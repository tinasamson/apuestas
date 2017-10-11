# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from django.core import mail


class Command(BaseCommand):

    def handle(self, *args, **options):
        connection = mail.get_connection()
        import ipdb; ipdb.set_trace()
        connection.open()

        mail0 = mail.EmailMessage(
            'Asunto 0',
            'Cuerpo del email 0',
            'dwarf1@gmail.com',
            ['pablodalmasso@gmail.com'],
            connection=connection
        )
        print mail0.send()

        mail1 = mail.EmailMessage(
            'Asunto 1',
            'Cuerpo del email 1',
            'dwarf1@gmail.com',
            ['sergioleyes@gmail.com'],
            connection=connection
        )
        print mail1.send()
        mail2 = mail.EmailMessage(
            'Asunto 2',
            'Cuerpo del email 2',
            'dwarf1@gmail.com',
            ['rubengocio@gmail.com'],
        )
        mail3 = mail.EmailMessage(
            'Asunto 3',
            'Cuerpo del email 3',
            'dwarf1@gmail.com',
            ['tec.bertola@gmail.com'],
        )
        print connection.send_messages([mail2, mail3])
        connection.close()
