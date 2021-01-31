from ..entities.faunadb_entity import get, get_multiple, get_by_ref_id, create, update, delete


def get_all_customers():
    try:
        return get_multiple('all_customers')
    except Exception as ex:
        raise ex


def get_customers_by_ref_id(id):
    try:
        return get_by_ref_id('customers', id)
    except Exception as ex:
        raise ex


def create_customers(data):
    try:
        return create('customers', data)
    except Exception as ex:
        raise ex


def update_customers(id, data):
    try:
        return update('customers', id, data)
    except Exception as ex:
        raise ex


def delete_customers(id):
    try:
        return delete('customers', id)
    except Exception as ex:
        raise ex
