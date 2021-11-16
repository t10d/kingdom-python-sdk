import pytest

from kingdom_sdk.adapters.message_bus import UnknownMessage


@pytest.mark.asyncio
async def test_message_bus_handling_command(
    uow, message_bus, example_command, example_command_handlers
):
    with uow:
        await message_bus.handle(example_command)

    mocked_handler = example_command_handlers[example_command.__class__]
    mocked_handler.assert_called_once()


@pytest.mark.asyncio
async def test_message_bus_handling_event(
    uow, message_bus, example_event, example_event_handlers
):
    with uow:
        await message_bus.handle(example_event)

    for mocked_handler in example_event_handlers[example_event.__class__]:
        mocked_handler.assert_called_once()


@pytest.mark.asyncio
async def test_message_bus_not_mapped_message_handler(
    uow, message_bus, example_unhandlable_command
):
    with pytest.raises(KeyError):
        await message_bus.handle(example_unhandlable_command)


@pytest.mark.asyncio
async def test_message_bus_handling_unknonw_message(uow, message_bus):
    with pytest.raises(UnknownMessage):
        await message_bus.handle("Not a message, it's a string!")
