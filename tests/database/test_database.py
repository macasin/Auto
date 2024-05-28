import pytest
from modules.common.database import Database

@pytest.mark.database
def test_databaseConnection():
    db= Database()
    db.test_connection()

@pytest.mark.database
def test_databaseCheckAllUsers():
    db=Database()
    users=db.get_allUsers()

    print(users)

@pytest.mark.database
def test_checkUserSergii():
    db=Database()
    user=db.get_UserAddressAndCityByName("Sergii")

    assert user[0][0]=="Kyiv" #test that check if the city has valid data
    assert user[0][1]=="Maydan Nezalezhnosti 1" #test that check if the address has valid data

@pytest.mark.database
def test_checkTheQuatityInProductAfterUpdate():
    db=Database()
    db.change_productsQuantityByID(25,1)
    water_qnt= db.get_showTheChangesInProductByID(1)

    assert water_qnt[0][0]==25 #test that check the quantity of water

@pytest.mark.database
def test_newAddedProduct():
    db=Database()
    db.add_newProduct(15, 'cookies', 'with chocolate', 30)
    water_qnt=db.get_showTheChangesInProductByID(15)

    assert water_qnt[0][0]==30 #test that check that new product was added with valid qnt

@pytest.mark.database
def test_dataDeleted():
    db=Database()
    db.delete_product(15)
    qnt=db.get_showTheChangesInProductByID(15)

    assert len(qnt)==0

 