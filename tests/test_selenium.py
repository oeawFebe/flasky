from selenium import webdriver
import re,threading,time,unittest
from app import create_app,db,fake
from app.models import Role, User, Post

class SeleniumTestCase(unittest.TestCase):
    client=None
    @classmethod
    def setUpClass(cls):
        options=webdriver.ChromeOptions()
        options.add_argument('headless')
        
        try:
            cls.client=webdriver.Chrome(options=options)#chrome_options deprecated
        except:
            pass

        if cls.client:
            cls.app=create_app("testing")
            cls.app_context=cls.app.app_context()
            cls.app_context.push()
            import logging
            logger=logging.getLogger("werkzeug")
            logger.setLevel("ERROR")

            db.create_all()
            Role.insert_roles()
            fake.users(10)
            fake.posts(10)

            admin_role=Role.query.filter_by(permissions=0xff).first()
            admin=User(email="john@example.com",username="john",password="cat",role=admin_role,confirmed=True)
            db.session.add(admin)
            db.session.commit()
            time.sleep(1)
            cls.server_thread=threading.Thread(target=cls.app.run,kwargs={
                "debug":"false",
                "use_reloader":"false",
                "use_debugger":"false"})
            cls.server_thread.start()
            time.sleep(1)
    @classmethod
    def tearDownClass(cls):
        if cls.client:
            cls.client.get("http://localhost:5000/shutdown")
            cls.client.quit()
            cls.server_thread.join()
            db.drop_all()
            db.session.remove()
            cls.app_context.pop()
    def setUp(self):
        if not self.client:
            self.skipTest("Web browser not available")
    def tearDown(self):
        pass
    def test_admin_home_page(self):
        self.client.get("http://localhost:5000/")
        self.assertTrue(re.search("Hello,\s+Stranger!",self.client.page_source))
        self.client.find_element_by_link_text("Log In").click()
        self.assertIn("<h1>Login</h1>",self.client.page_source)

        #login
        self.client.find_element_by_name("email").send_keys("john@example.com")
        self.client.find_element_by_name("password").send_keys("cat")

        self.client.find_element_by_name("submit").click()
        self.assertTrue(re.search("Hello,\s+john!", self.client.page_source))

        #navigate to users profile page
        self.client.find_element_by_link_text("Profile").click()
        self.assertIn("<h1>john</h1>",self.client.page_source)