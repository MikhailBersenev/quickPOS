"""
Pydantic схемы для quickPOS API
"""

from .user import UserBase, UserCreate, UserUpdate, UserResponse
from .role import RoleBase, RoleCreate, RoleUpdate, RoleResponse
from .position import PositionBase, PositionCreate, PositionUpdate, PositionResponse
from .employee import EmployeeBase, EmployeeCreate, EmployeeUpdate, EmployeeResponse
from .goodcat import GoodCatBase, GoodCatCreate, GoodCatUpdate, GoodCatResponse
from .good import GoodBase, GoodCreate, GoodUpdate, GoodResponse
from .batch import BatchBase, BatchCreate, BatchUpdate, BatchResponse
from .barcode import BarcodeBase, BarcodeCreate, BarcodeUpdate, BarcodeResponse
from .discount import DiscountBase, DiscountCreate, DiscountUpdate, DiscountResponse
from .vatrate import VATRateBase, VATRateCreate, VATRateUpdate, VATRateResponse
from .item import ItemBase, ItemCreate, ItemUpdate, ItemResponse
from .sale import SaleBase, SaleCreate, SaleUpdate, SaleResponse
from .check import CheckBase, CheckCreate, CheckUpdate, CheckResponse, CheckWithSales
from .service import ServiceBase, ServiceCreate, ServiceUpdate, ServiceResponse
from .auth import Token, TokenData, LoginRequest, LoginResponse, PasswordChange
from .pos import (
    ProductSearchRequest,
    ProductInfo,
    CartItem,
    CheckCreateRequest,
    CheckSummary,
)

__all__ = [
    # User
    "UserBase",
    "UserCreate",
    "UserUpdate",
    "UserResponse",
    # Role
    "RoleBase",
    "RoleCreate",
    "RoleUpdate",
    "RoleResponse",
    # Position
    "PositionBase",
    "PositionCreate",
    "PositionUpdate",
    "PositionResponse",
    # Employee
    "EmployeeBase",
    "EmployeeCreate",
    "EmployeeUpdate",
    "EmployeeResponse",
    # GoodCat
    "GoodCatBase",
    "GoodCatCreate",
    "GoodCatUpdate",
    "GoodCatResponse",
    # Good
    "GoodBase",
    "GoodCreate",
    "GoodUpdate",
    "GoodResponse",
    # Batch
    "BatchBase",
    "BatchCreate",
    "BatchUpdate",
    "BatchResponse",
    # Barcode
    "BarcodeBase",
    "BarcodeCreate",
    "BarcodeUpdate",
    "BarcodeResponse",
    # Discount
    "DiscountBase",
    "DiscountCreate",
    "DiscountUpdate",
    "DiscountResponse",
    # VATRate
    "VATRateBase",
    "VATRateCreate",
    "VATRateUpdate",
    "VATRateResponse",
    # Item
    "ItemBase",
    "ItemCreate",
    "ItemUpdate",
    "ItemResponse",
    # Sale
    "SaleBase",
    "SaleCreate",
    "SaleUpdate",
    "SaleResponse",
    # Check
    "CheckBase",
    "CheckCreate",
    "CheckUpdate",
    "CheckResponse",
    "CheckWithSales",
    # Service
    "ServiceBase",
    "ServiceCreate",
    "ServiceUpdate",
    "ServiceResponse",
    # Auth
    "Token",
    "TokenData",
    "LoginRequest",
    "LoginResponse",
    "PasswordChange",
    # POS
    "ProductSearchRequest",
    "ProductInfo",
    "CartItem",
    "CheckCreateRequest",
    "CheckSummary",
]

# Разрешаем forward references после импорта всех схем
from .check import CheckWithSales
CheckWithSales.model_rebuild()

from .auth import LoginResponse
LoginResponse.model_rebuild()

