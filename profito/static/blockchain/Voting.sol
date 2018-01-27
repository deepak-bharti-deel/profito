pragma solidity ^0.4.18;

contract Voting {
 
  address public buyer;
  address public seller;
  address public arbiter;
  
  
   function Voting (address _arbiter) payable {
    arbiter = _arbiter;
  }


  function getFromCompany(uint balance,address _seller){
    seller = _seller;
    if(seller.balance>balance){
      arbiter.send(balance);
    }
  }

  function distributeBalance(uint balance,address _buyer){
    buyer = _buyer;
    if(arbiter.balance>balance){
      buyer.send(balance);
    }
  }

  function getBalance() constant returns (uint) {
    return this.balance;
  }

}
