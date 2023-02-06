# fluency-simple-stake ![build](https://github.com/manosbatsis/fluency-simple-stake/actions/workflows/main.yaml/badge.svg)

## Requirements 

- Setup [node](https://nodejs.org) and [brownie](https://eth-brownie.readthedocs.io/en/stable/)
- Add a dummy _.env_ file:
 
  `touch .env`
- Install [Ganache](https://trufflesuite.com/ganache/):
  
  `npm install -g ganache`

## Build and Test

```
brownie test
```

## Credits

Based on https://github.com/GeneralDido/blockchain-examples/tree/main/simple_proof_of_stake
