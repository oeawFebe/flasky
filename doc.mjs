// Reference https://polkadot.js.org/docs/api/start/api.tx

// Import by npm init and npm install @polkadot/api
import { ApiPromise, WsProvider } from '@polkadot/api';

async function myreturnfunc(blockNumber) {

    // API interface; do not forget to run polkadot binary (alias kusama in this)
    const wsProvider = new WsProvider('wss://kusama-rpc.polkadot.io');
    const api = await ApiPromise.create({ provider: wsProvider });
    const blockHash = await api.rpc.chain.getBlockHash(blockNumber);
    // console.log(blockHash.toHex());
    const ADDR = "HU6TSsvA84GKrTiyArBHiFDVBSLHNr5Ki3qPV7T8WKyVJaz";
    Promise.all([
        api.query.system.account.at(blockHash.toHex(), ADDR),
    ]).then(answer => {
        let bigintstr = String(answer[0].data.free);
        console.log(bigintstr);
        process.exit(0);
    });
}

// const blockNumber = 11760051;
const blockNumber = process.argv[2]
myreturnfunc(blockNumber);


// 2022-03-10 02:29:03        API/INIT: RPC methods not decorated: author_unsubscribesubmitAndWatchExtrinsic, childstate_getChildReadProof, getKeysPagedAt, system_nextIndex
// [
//   Type(5) [Map] {
//     'nonce' => <BN: f>,
//     'consumers' => <BN: 2>,
//     'providers' => <BN: 1>,
//     'sufficients' => <BN: 0>,
//     'data' => Type(4) [Map] {
//       'free' => <BN: 46e9d689afdb>,
//       'reserved' => <BN: add8cd0d8>,
//       'miscFrozen' => <BN: 4484067a9bfa>,
//       'feeFrozen' => <BN: 4484067a9bfa>,
//       initialU8aLength: 64,
//       free: [Getter],
//       reserved: [Getter],
//       miscFrozen: [Getter],
//       feeFrozen: [Getter]
//     },
//     initialU8aLength: 80,
//     nonce: [Getter],
//     consumers: [Getter],
//     providers: [Getter],
//     sufficients: [Getter],
//     data: [Getter],
//     createdAtHash: Type(32) [Uint8Array] [
//       39,
//       111,
//       51,
//       33,
//       65,
//       141,
//       123,
//       168,
//       205,
//       177,
//       66,
//       81,
//       82,
//       125,
//       142,
//       88,
//       4,
//       13,
//       210,
//       76,
//       189,
//       210,
//       68,
//       90,
//       185,
//       112,
//       4,
//       133,
//       248,
//       177,
//       144,
//       128,
//       registry: [TypeRegistry],
//       initialU8aLength: 32
//     ]
//   }
// ]
