from typing import TypedDict, Optional, Literal

from method.resource import Resource
from method.configuration import Configuration
from method.errors import ResourceError

AccountBalanceStatusLiterals = Literal[
    'completed',
    'in_progress',
    'pending',
    'failed'
]

class AccountBalances(TypedDict):
    id: str
    status: AccountBalanceStatusLiterals
    balance: Optional[int]
    error: Optional[ResourceError]
    created_at: str
    updated_at: str

class AccountBalancesResource(Resource):
    def __init__(self, config: Configuration):
        super(AccountBalancesResource, self).__init__(config.add_path('balances'))

    def retrieve(self, bal_id: str) -> AccountBalances:
        return super(AccountBalancesResource, self)._get_with_id(bal_id)

    def create(self) -> AccountBalances:
        return super(AccountBalancesResource, self)._create({})