from dataclasses import dataclass


@dataclass
class Wallet():
    '''
    A user's wallet contains all the balances of the tokens the user owns
    '''
    token: str
    balance: float = 0.0
    
    def update_balance():
        '''
        Takes
        
        '''


# Transactions are 

@dataclass
class Transfer():
    '''
    Transfer class
    '''
    sender: str
    receiver: str
    token: str
    decimals: int
    amount: float
    
    def 
    
class DaiTransfer(Transfer):
    
    