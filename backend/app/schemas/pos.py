from pydantic import BaseModel, Field
from typing import Optional, List
from .good import GoodResponse
from .batch import BatchResponse


class ProductSearchRequest(BaseModel):
    """Схема для поиска товара"""
    barcode: Optional[str] = Field(None, description="Штрих-код товара")
    good_id: Optional[int] = Field(None, description="ID товара")
    name: Optional[str] = Field(None, description="Название товара (поиск)")


class ProductInfo(BaseModel):
    """Информация о товаре для POS"""
    good: GoodResponse = Field(..., description="Информация о товаре")
    batches: List[BatchResponse] = Field(default_factory=list, description="Доступные партии")
    total_quantity: int = Field(..., description="Общее количество на складе")
    min_price: float = Field(..., description="Минимальная цена")
    max_price: float = Field(..., description="Максимальная цена")


class CartItem(BaseModel):
    """Позиция в корзине"""
    item_id: Optional[int] = Field(None, description="ID позиции (если уже создана)")
    batch_id: Optional[int] = Field(None, description="ID партии")
    service_id: Optional[int] = Field(None, description="ID услуги")
    quantity: int = Field(..., gt=0, description="Количество")
    price: float = Field(..., gt=0, description="Цена за единицу")
    vat_rate_id: int = Field(..., description="ID ставки НДС")
    comment: Optional[str] = Field(None, description="Комментарий")


class CheckCreateRequest(BaseModel):
    """Схема для создания чека с товарами"""
    employee_id: int = Field(..., description="ID сотрудника")
    items: List[CartItem] = Field(..., min_items=1, description="Список товаров/услуг")
    discount_amount: float = Field(0, ge=0, description="Сумма скидки")
    comment: Optional[str] = Field(None, description="Комментарий к чеку")


class CheckSummary(BaseModel):
    """Сводка по чеку"""
    check_id: int = Field(..., description="ID чека")
    total_amount: float = Field(..., description="Общая сумма")
    discount_amount: float = Field(..., description="Сумма скидки")
    final_amount: float = Field(..., description="Итоговая сумма к оплате")
    items_count: int = Field(..., description="Количество позиций")
    date: str = Field(..., description="Дата и время чека")

