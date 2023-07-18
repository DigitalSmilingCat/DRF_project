valid_pereval_test_data = {
            "beauty_title": "Название препятствия 1",
            "title": "Название вершины 1",
            "other_titles": "Другое название 1",
            "connect": "",
            "user": {
                "email": "user1@mail.ru",
                "fam": "Фамилия 1",
                "name": "Имя 1",
                "otc": "Отчество 1",
                "phone": "+111111"
              },
            "coords": {
                "latitude": 11.1,
                "longitude": 22.2,
                "height": 333
              },
            "level": {
                "winter": "A1",
                "summer": "1B",
                "autumn": "C1",
                "spring": "1D"
              },
            "images": [
                {
                  "title": "Название 1",
                  "data": "https://example.com/image1.jpg"
                },
                {
                    "title": "Название 2",
                    "data": "https://example.com/image2.jpg"
                }
              ]
            }

missing_user_test_data = {
            "beauty_title": "Название препятствия 1",
            "title": "Название вершины 1",
            "other_titles": "Другое название 1",
            "connect": "",
            "coords": {
                "latitude": 11.1,
                "longitude": 22.2,
                "height": 333
              },
            "level": {
                "winter": "",
                "summer": "A1",
                "autumn": "1B",
                "spring": ""
              },
            "images": [
                {
                  "title": "Название 1",
                  "data": "https://example.com/image1.jpg"
                },
                {
                    "title": "Название 2",
                    "data": "https://example.com/image2.jpg"
                }
              ]
            }

missing_coords_test_data = {
            "beauty_title": "Название препятствия 1",
            "title": "Название вершины 1",
            "other_titles": "Другое название 1",
            "connect": "",
            "user": {
                "email": "user1@mail.ru",
                "fam": "Фамилия1",
                "name": "Имя1",
                "otc": "Отчество1",
                "phone": "+111111111"
              },
            "level": {
                "winter": "",
                "summer": "A1",
                "autumn": "1B",
                "spring": ""
              },
            "images": [
                {
                  "title": "Название 1",
                  "data": "https://example.com/image1.jpg"
                },
                {
                    "title": "Название 2",
                    "data": "https://example.com/image2.jpg"
                }
              ]
            }

missing_level_test_data = {
            "beauty_title": "Название препятствия 1",
            "title": "Название вершины 1",
            "other_titles": "Другое название 1",
            "connect": "",
            "user": {
                "email": "user1@mail.ru",
                "fam": "Фамилия1",
                "name": "Имя1",
                "otc": "Отчество1",
                "phone": "+111111111"
              },
            "coords": {
                "latitude": 11.1,
                "longitude": 22.2,
                "height": 333
              },
            "images": [
                {
                  "title": "Название 1",
                  "data": "https://example.com/image1.jpg"
                },
                {
                    "title": "Название 2",
                    "data": "https://example.com/image2.jpg"
                }
              ]
            }

missing_images_test_data = {
            "beauty_title": "Название препятствия 1",
            "title": "Название вершины 1",
            "other_titles": "Другое название 1",
            "connect": "",
            "user": {
                "email": "user1@mail.ru",
                "fam": "Фамилия1",
                "name": "Имя1",
                "otc": "Отчество1",
                "phone": "+111111111"
              },
            "coords": {
                "latitude": 11.1,
                "longitude": 22.2,
                "height": 333
              },
            "level": {
                "winter": "",
                "summer": "A1",
                "autumn": "1B",
                "spring": ""
              },
            }

patch_valid_payload = {
            "title": "Новое название",
            "user": {
                "email": "user1@mail.ru",
                "fam": "Фамилия 1",
                "name": "Имя 1",
                "otc": "Отчество 1",
                "phone": "+111111"
            }
        }

patch_changed_user_payload = {
            "title": "Новое название",
            "user": {
                "email": "user1@mail.ru",
                "fam": "Другая Фамилия",
                "name": "Имя 1",
                "otc": "Отчество 1",
                "phone": "+111111"
            }
        }

patch_invalid_coords_payload = {
            "user": {
                "email": "user1@mail.ru",
                "fam": "Фамилия 1",
                "name": "Имя 1",
                "otc": "Отчество 1",
                "phone": "+111111"
            },
            "coords": {
                "height": "abc",
                "latitude": "null",
                "longitude": "null"
              }
        }

patch_not_new_status_payload = {
            "title": "Новое название",
            "user": {
                "email": "user3@mail.ru",
                "fam": "Фамилия 3",
                "name": "Имя 3",
                "otc": "Отчество 3",
                "phone": "+333333333"
            }
        }

put_changed_user_payload = {
            "beauty_title": "Название препятствия 1",
            "title": "Название вершины 1",
            "other_titles": "Другое название 1",
            "connect": "",
            "user": {
                "email": "user1@mail.ru",
                "fam": "Другая фамилия",
                "name": "Имя 1",
                "otc": "Отчество 1",
                "phone": "+111111111"
              },
            "coords": {
                "latitude": 11.1,
                "longitude": 22.2,
                "height": 333
              },
            "level": {
                "winter": "",
                "summer": "A1",
                "autumn": "1B",
                "spring": ""
              },
            "images": [
                {
                  "title": "Название 1",
                  "data": "https://example.com/image1.jpg"
                },
                {
                    "title": "Название 2",
                    "data": "https://example.com/image2.jpg"
                }
              ]
            }

put_not_new_status_payload = {
            "status": "pending",
            "beauty_title": "Название препятствия 1",
            "title": "Название вершины 1",
            "other_titles": "Другое название 1",
            "connect": "",

            "user": {
                "email": "user1@mail.ru",
                "fam": "Другая фамилия",
                "name": "Имя 1",
                "otc": "Отчество 1",
                "phone": "+111111111"
              },
            "coords": {
                "latitude": 11.1,
                "longitude": 22.2,
                "height": 333
              },
            "level": {
                "winter": "",
                "summer": "A1",
                "autumn": "1B",
                "spring": ""
              },
            "images": [
                {
                  "title": "Название 1",
                  "data": "https://example.com/image1.jpg"
                },
                {
                    "title": "Название 2",
                    "data": "https://example.com/image2.jpg"
                }
              ]
            }