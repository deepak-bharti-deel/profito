Web3 = require('web3');
solc = require('solc');
fs = require('fs');

web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
console.log("Connected to Blockchain !!");

code = fs.readFileSync("Voting.sol").toString();

console.log("Compiling realEstate.sol ...");
compiledCode = solc.compile( code );
console.log("Compiled successfully!!");

abi = JSON.parse( compiledCode.contracts[":Voting"].interface );
byteCode = compiledCode.contracts[':Voting'].bytecode ;

var buyer;
var seller;
var arbiter; 

arbiter = web3.eth.accounts[0];

realEstateContract =  web3.eth.contract(abi) ;
console.log("Deploying ...")
deployedContract = realEstateContract.new(arbiter,{data: byteCode , from: web3.eth.accounts[0] , gas: 3000000 },
( e , contract )=>{
      if( contract.address )
        {
          console.log("Deployed successfully...\n\n\nDeployed Address : " + contract.address );
          console.log("Use the above deployed address in realEstate.js ...\n\n");
        }
});


function collectMoney(){
  	var id=document.getElementById('id').value;
  	var amount=document.getElementById('amount').value;
//get from web
	buyer = web3.eth.accounts[id];
	deployedContract.getFromCompany(amount,buyer,{ from: buyer , gas: 3000000 ,gasPrice: 5});

}

function disributeLikes(){
	var id=[1,2,3,4,5];
	var amount;
	//get from web
	var i;
	for(i=0;i<id.length;i++){
		buyer = web3.eth.accounts[id[i]];
		deployedContract.distributeBalance(amount,buyer,{from : arbiter , gas: 3000000 ,gasPrice: 5});
	}
}

function distributeShares(){
	var id=[1,2,3,4,5];
	var amount;
	//get from web
	var i;
	for(i=0;i<id.length;i++){
		buyer = web3.eth.accounts[id[i]];
		deployedContract.distributeBalance(amount,buyer,{from : arbiter , gas: 3000000 ,gasPrice: 5});
	}
}

function refundBack(){
	var id;
	var amount;

	seller = web3.eth.accounts[id];
	deployedContract.distributeBalance(amount,seller,{from : arbiter , gas: 3000000 ,gasPrice: 5});
}



