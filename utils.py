from dcim.models import Cable, Device

def trace_cable(start_device, start_port):
    """
    Рекурсивная функция для трассировки кабеля до конечной точки.
    """
    current_device = start_device
    current_port = start_port
    path = []

    while True:
        # Получаем кабель, подключенный к текущему порту
        cable = Cable.objects.filter(a_terminations__device=current_device, a_terminations__name=current_port).first()
        if not cable:
            cable = Cable.objects.filter(b_terminations__device=current_device, b_terminations__name=current_port).first()

        if not cable:
            break  # Кабель не найден, завершаем трассировку

        # Добавляем текущий кабель в путь
        path.append({
            'cable': cable.id,
            'device': current_device.name,
            'port': current_port
        })

        # Определяем следующее устройство и порт
        if cable.a_terminations.device == current_device:
            next_device = cable.b_terminations.device
            next_port = cable.b_terminations.name
        else:
            next_device = cable.a_terminations.device
            next_port = cable.a_terminations.name

        # Переходим к следующему устройству
        current_device = next_device
        current_port = next_port

    return path
