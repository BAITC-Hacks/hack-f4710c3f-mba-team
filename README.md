# hack-f4710c3f-mba-team

Hackathon team repository for MBA Team.

## Командная работа

- `main` — только проверенная версия проекта, готовая к демонстрации.
- `develop` — общая ветка, в которую объединяется работа команды.
- Для каждой задачи создавайте отдельную ветку от `develop`: `feature/<задача>` или `fix/<ошибка>`.
- Не делайте прямые изменения в `main` и `develop`: отправляйте изменения через Pull Request в `develop`.
- Перед началом работы обновляйте ветку `develop`; перед Pull Request подтягивайте её в свою ветку и решайте конфликты.

```bash
git checkout develop
git pull origin develop
git checkout -b feature/название-задачи
# ... работа над задачей ...
git add .
git commit -m "Краткое описание изменения"
git push -u origin feature/название-задачи
```

После `push` создайте Pull Request из своей ветки в `develop` на GitHub. Когда всё протестировано, интегратор команды создаёт Pull Request из `develop` в `main`.
