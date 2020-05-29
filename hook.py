from app.objects.c_obfuscator import Obfuscator
from app.utility.base_world import BaseWorld
from plugins.robinhood.app.robinhood_svc import RobinhoodService

name = 'Robinhood'
description = 'A stockpile of abilities, adversaries, payloads and planners'
address = '/plugin/robinhood/gui'
access = BaseWorld.Access.RED


async def enable(services):
    robinhood_svc = RobinhoodService(services)
    services.get('app_svc').application.router.add_route('GET', '/plugin/robinhood/gui', robinhood_svc.splash)
    await services.get('file_svc').add_special_payload('.donut', 'plugins.robinhood.app.donut.donut_handler')
    await robinhood_svc.data_svc.store(
        Obfuscator(name='plain-text',
                   description='Does no obfuscation to any command, instead running it in plain text',
                   module='plugins.robinhood.app.obfuscators.plain_text')
    )
    await robinhood_svc.data_svc.store(
        Obfuscator(name='base64',
                   description='Obfuscates commands in base64',
                   module='plugins.robinhood.app.obfuscators.base64_basic')
    )
    await robinhood_svc.data_svc.store(
        Obfuscator(name='base64jumble',
                   description='Obfuscates commands in base64, then adds characters to evade base64 detection. '
                               'Disclaimer: this may cause duplicate links to run.',
                   module='plugins.robinhood.app.obfuscators.base64_jumble')
    )
    await robinhood_svc.data_svc.store(
        Obfuscator(name='caesar cipher',
                   description='Obfuscates commands through a caesar cipher algorithm, which uses a randomly selected '
                               'shift value.',
                   module='plugins.robinhood.app.obfuscators.caesar_cipher')
    )
    await robinhood_svc.data_svc.store(
        Obfuscator(name='base64noPadding',
                   description='Obfuscates commands in base64, then removes padding',
                   module='plugins.robinhood.app.obfuscators.base64_no_padding')
    )
    await robinhood_svc.data_svc.store(
        Obfuscator(name='steganography',
                   description='Obfuscates commands through image-based steganography',
                   module='plugins.robinhood.app.obfuscators.steganography')
    )
