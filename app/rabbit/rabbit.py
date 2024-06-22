import os

import aio_pika

RABBITMQ_URL = os.getenv("RABBITMQ_URL")


async def send_message(message: str):
    connection = await aio_pika.connect_robust(RABBITMQ_URL)
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("auth_queue")
        await channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()),
            routing_key=queue.name,
        )
