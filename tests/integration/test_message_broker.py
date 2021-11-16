def test_message_broker_publish(message_broker, example_command):
    message_broker.publish("test", example_command)
