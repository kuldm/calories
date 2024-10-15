from fastapi import HTTPException, status


class FoodstuffsExceptions(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class FoodstuffMissingException(FoodstuffsExceptions):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Поле 'name' не может быть пустым"


class FoodstuffAlreadyExistException(FoodstuffsExceptions):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Продукт уже существует"

    def __init__(self, name):
        self.detail = f"Продукт '{name}' уже существует"


class FoodstuffAbsentException(FoodstuffsExceptions):
    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self, id):
        self.detail = f"Продукта с id: {id} не существует"


class OkStatusCode(FoodstuffsExceptions):
    status_code = status.HTTP_200_OK
    detail = "Запись удалена"


class LinkM2MException(FoodstuffsExceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = "Невозможно удалить, поскольку на значение есть ссылка в другой таблице."
