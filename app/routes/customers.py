from fastapi import APIRouter
from ..models.customer_model import Customer, Address, CreditCard, NewCustomer
from ..services.customers_service import create_customers as create_customer_record, get_all_customers, get_customers_by_ref_id, update_customers, delete_customers

router = APIRouter()


@router.get("/", tags=["customer"])
async def list_customers():
    """
    Lists all of the customer records in FaunaDB 
    """
    response = get_all_customers()
    return response


@router.get("/{customer_id}", tags=["customer"])
async def get_customers_by_id(customer_id: str):
    """
    Gets a customer record by it's ref ID 
    """
    return get_customers_by_ref_id(customer_id)


@router.post("/", tags=["customer"], response_model=Customer)
async def create_customers(new_customer: NewCustomer):
    """
    Create a customer record 
    """
    return create_customer_record(dict(new_customer))


@router.put("/{customer_id}", tags=["customer"], response_model=Customer)
async def update_customer(customer_id: str, customer: Customer):
    """
    Update a customer record
    """
    return update_customer({id: customer_id, **customer.dict()})
