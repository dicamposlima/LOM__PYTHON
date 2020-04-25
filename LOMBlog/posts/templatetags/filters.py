from django import template

register = template.Library()


@register.filter(name='plural_comentarios')
def plural_comentarios(num_comentarios: int):
    try:
        num_comentarios = int(num_comentarios)
        if num_comentarios == 0:
            return f'Nenhum comentário'
        elif num_comentarios == 1:
            return f'{num_comentarios} COMENTARIO'
        else:
            return f'{num_comentarios} COMENTARIOS'
    except ValueError as e:
        return f'{num_comentarios} COMENTARIOS'
