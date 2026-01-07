![main](img/1.png)
На последнем шаге лабораторной работы Docker Registry был запущен с подключённым внешним хранилищем (registry-data), смонтированным в /var/lib/registry.
После публикации образа hello-world в registry, в каталоге registry-data была сформирована стандартная структура Docker Registry v2 (docker/registry/v2/repositories, blobs), что подтверждает успешное сохранение образа вне контейнера registry.
![main](img/2.png)
![main](img/3.png)
![main](img/4.png)
Registry настроен на работу по протоколу HTTPS с использованием TLS-сертификата. Наличие HTTPS подтверждено выводом curl -vk (TLS handshake). Для доступа включена Basic Authentication через htpasswd. Без учётных данных сервер возвращает 401 Unauthorized. При передаче корректных учётных данных moby:gordon запрос к /v2/ завершается успешно с кодом 200 OK, что подтверждает успешную аутентификацию.
