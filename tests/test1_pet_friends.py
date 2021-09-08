import api
from settings import valid_email, valid_password, invalid_email, invalid_age
import os

pf = api.PetFriends()


def test_successful_add_new_pet_without_foto(name='Буся', animal_type='терьер',
                                             age='4', pet_photo=''):
    """Проверяем что можно добавить питомца без фото"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_foto(auth_key, name, animal_type, age)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_successful_update_self_pet_add_photo(pet_photo='images/masya.jpg'):
    """Проверяем возможность добавления фото к питомцу"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_add_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['pet_photo'] is not ''  # (выдаёт ошибку)

    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_get_api_key_for_invalid_user(email=invalid_email, password=valid_password):
    """" Проверяем, что запрос ключа от несуществующего пользователя не возвращает
    статус 200"""
    # Отправляем запрос и сохряняем полученный ответ с кодом статуса в status
    status = pf.get_api_key(email, password)
    # Проверяем:
    assert status != 200


def test_get_all_pets_with_invalid_key(filter=''):
    """ Проверяем, что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key.
    Далее используя этого ключ запрашиваем список всех питомцев и проверяем,
    что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(invalid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200


def test_add_new_pet_with_invalid_age(name='Морковка', animal_type='такса',
                                      age=invalid_age, pet_photo='images/masya.jpg'):
    """Проверяем, что возраст питомца нельзя обозначить буквами"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result[age] is int

def test_add_new_pet_with_big_age(name='Кеша', animal_type='удав',
                                     age='9999', pet_photo='images/udav.jpg'):
    """Проверяем, что можно добавить питомца с некорректным возрастом"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_without_age(name='Кеша', animal_type='удав',
                                     age='', pet_photo='images/udav.jpg'):
    """Проверяем что можно добавить питомца с отсутствием даннных о возрасте"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_without_animal_type(name='Вася', animal_type='',
                                     age='7', pet_photo='images/enot.jpg'):
    """Проверяем что можно добавить питомца с отсутствием данных о породе"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_without_name(name='', animal_type='Енот',
                                     age='7', pet_photo='images/enot.jpg'):
    """Проверяем что можно добавить питомца с отсутствием данных об имени"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_without_name_age(name='', animal_type='Енот',
                                     age='', pet_photo='images/enot.jpg'):
    """Проверяем что можно добавить питомца с отсутствием данных об имени и возрасте"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_without_name_age_animal_type(name='', animal_type='',
                                     age='', pet_photo='images/enot.jpg'):
    """Проверяем что можно добавить питомца только с фото"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name
