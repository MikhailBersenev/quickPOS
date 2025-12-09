from sqlalchemy import Column, Integer, String, Boolean, Date, Time, Double
from app.database import Base

class Users(Base):
    __tablename__ = 'public.users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    roleId = Column(Integer, nullable=False)
    isDeleted = Column(Boolean, nullable=True)

class Roles(Base):
    __tablename__ = 'public.roles'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    level = Column(Integer, nullable=False)
    isBlocked = Column('isblocked', Boolean, nullable=True)
    isDeleted = Column('isdeleted', Boolean, nullable=True)

class Positions(Base):
    __tablename__ = 'public.positions'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    level = Column(Integer, nullable=False)
    isBlocked = Column('isblocked', Boolean, nullable=True)
    isDeleted = Column('isdeleted', Boolean, nullable=True)

class Barcodes(Base):
    __tablename__ = 'public.barcodes'
    id = Column(Integer, primary_key=True)
    barcode = Column(String, nullable=False)
    batchId = Column('batchid', Integer, nullable=False)
    updateDate = Column('updatedate', Date, nullable=False)
    isDeleted = Column('isdeleted', Boolean, nullable=True)

class Batches(Base):
    __tablename__ = 'public.batches'
    id = Column(Integer, primary_key=True)
    goodId = Column('goodid', Integer, nullable=False)
    price = Column(Double, nullable=False)
    qnt = Column(Integer, nullable=False)
    batchNumber = Column('batchnumber', String, nullable=True)
    prodDate = Column('proddate', Date, nullable=False)
    expDate = Column('expdate', Date, nullable=False)
    writtenOff = Column('writtenoff', Boolean, nullable=True)
    updateDate = Column('updatedate', Date, nullable=False)
    employeeId = Column('employeeId', Integer, nullable=False)
    isDeleted = Column('isDeleted', Boolean, nullable=True)

class Checks(Base):
    __tablename__ = 'public.checks'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    totalAmount = Column('totalamount', Double, nullable=False)
    discountAmount = Column('discountamount', Double, nullable=False)
    employeeId = Column('employeeid', Integer, nullable=False)
    isDeleted = Column('isdeleted', Boolean, nullable=True)

class Discounts(Base):
    __tablename__ = 'public.discounts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    percent = Column(Double, nullable=True)
    sum = Column(Double, nullable=False)
    isDeleted = Column('isdeleted', Boolean, nullable=True)

class Employees(Base):
    __tablename__ = 'public.employees'
    id = Column(Integer, primary_key=True)
    lastName = Column('lastname', String, nullable=False)
    firstName = Column('firstname', String, nullable=False)
    middleName = Column('middlename', String, nullable=True)
    positionId = Column('positionid', Integer, nullable=False)
    userId = Column('userid', Integer, nullable=False)
    updateDate = Column('updatedate', Date, nullable=False)
    isDeleted = Column('isdeleted', Boolean, nullable=True)

class GoodCats(Base):
    __tablename__ = 'public.goodcats'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    updateDate = Column('updatedate', Date, nullable=False)
    isDeleted = Column('isdeleted', Boolean, nullable=True)

class Goods(Base):
    __tablename__ = 'public.goods'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    categoryId = Column('categoryid', Integer, nullable=False)
    imageUrl = Column('imageurl', String, nullable=True)
    isActive = Column('isactive', Boolean, nullable=False)
    discountId = Column('discountid', Integer, nullable=False)
    updateDate = Column('updatedate', Date, nullable=False)
    employeeId = Column('employeeId', Integer, nullable=False)
    isDeleted = Column('isdeleted', Boolean, nullable=True)

class Items(Base):
    __tablename__ = 'public.items'
    id = Column(Integer, primary_key=True)
    batchId = Column('batchid', Integer, nullable=True)
    serviceId = Column('serviceid', Integer, nullable=True)
    isDeleted = Column('isdeleted', Boolean, nullable=True)

class Sales(Base):
    __tablename__ = 'public.sales'
    id = Column(Integer, primary_key=True)
    itemId = Column('itemid', Integer, nullable=False)
    qnt = Column(Integer, nullable=False)
    VATRateId = Column('vatrateid', Integer, nullable=False)
    sum = Column(Double, nullable=False)
    comment = Column(String, nullable=True)
    CheckId = Column('checkid', Integer, nullable=False) 
    isDeleted = Column('isdeleted', Boolean, nullable=True)

class Services(Base):
    __tablename__ = 'public.services'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Double, nullable=False)
    updateDate = Column(Date, nullable=False)
    comment = Column(String, nullable=True)
    CheckId = Column('checkid', Integer, nullable=False) 
    isDeleted = Column('isdeleted', Boolean, nullable=True)

class VATRates(Base):
    __tablename__ = 'public.vatrates'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rate = Column(Double, nullable=False)
    isDeleted = Column('isdeleted', Boolean, nullable=True)

