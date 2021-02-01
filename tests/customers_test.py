from app.services.customers_service import create_customers, get_customers_by_ref_id, delete_customers, update_customers, get_all_customers
from app.models.customer_model import NewCustomer


class Store:
    """
    This holds the state as the tests are executed sequentially
    """
    ID = None
    CustomerRecord = None


def creating_customer():
    """
    Tests creating a customer

    Returns:
        None
    """
    data = {
        'firstName': 'Adam',
        'lastName': 'Manuel',
        'telephone': '8326220272',
    }
    customer = NewCustomer(**data)
    response = create_customers(dict(customer))
    Store.CustomerRecord = response
    assert(response is not None)
    response_without_key = dict(response)
    refid = response_without_key.pop('ref_id')
    Store.ID = refid
    assert(refid is not None)
    assert(response_without_key == dict(data))
    return refid


def getting_customer_by_ID():
    """
    Tests finding that new customer by it's ID

    Returns:
        None
    """
    customer = get_customers_by_ref_id(Store.ID)
    assert(customer == Store.CustomerRecord)


def test():
    creating_customer()
    getting_customer_by_ID()
