"""MPC300 PLC and communicator."""
from ..helper.convert import int_to_hex
from ..helper.message import Message
from ..communicator.abstract_communicator import AbstractCommunicator


class Mpc300(AbstractCommunicator):
    """MPC300 implementation."""

    def read_word(self, plc, address) -> str:
        """Read word value from PLC."""
        message = Message.build_message(plc, "*", 0x44, int_to_hex(address, 4))
        data = self._tcp_client.send_and_receive(message)
        value = data[len(data) - 4 : len(data)]
        return "0x" + value

    def write_word(self, plc, address, value: int) -> str:
        """Write word value to PLC."""
        message = Message.build_message(
            plc,
            "*",
            0x45,
            int_to_hex(address, 4) + int_to_hex(value, 4),
        )
        data = self._tcp_client.send_and_receive(message)
        value = data[len(data) - 4 : len(data)]
        return "0x" + str(value)

    def read_bit(self, plc, address, bit_index) -> bool:
        """Read boolean value from PLC."""
        mask = 2 ** bit_index
        message = Message.build_message(
            plc, "*", 0x2A, int_to_hex(address, 4) + int_to_hex(mask, 2)
        )
        data = self._tcp_client.send_and_receive(message)
        value = data[len(data) - 2 : len(data)]
        return int(value) == 1

    def write_bit(self, plc, address, bit_index, value: bool) -> bool:
        """Write boolean value to PLC."""
        mask = 2 ** bit_index
        value_int = 0
        if value:
            value_int = 1
        message = Message.build_message(
            plc,
            "*",
            0x2B,
            int_to_hex(address, 4)
            + int_to_hex(mask, 2)
            + int_to_hex(value_int, 2),
        )
        data = self._tcp_client.send_and_receive(message)
        value = data[len(data) - 2 : len(data)]
        return int(value) == 1
