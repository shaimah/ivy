# global
import ivy
import ivy.functional.frontends.paddle as paddle
from ivy.func_wrapper import (
    with_unsupported_dtypes,
    handle_out_argument,
    with_supported_dtypes,
)
from ivy.functional.frontends.paddle.func_wrapper import (
    to_ivy_arrays_and_back,
)


@with_unsupported_dtypes(
    {"2.4.2 and below": ("uint8", "int8", "int16", "complex64", "complex128")}, "paddle"
)
@to_ivy_arrays_and_back
def equal(x, y, /, *, name=None):
    return ivy.equal(x, y)


@with_unsupported_dtypes(
    {"2.4.2 and below": ("uint8", "int8", "int16", "complex64", "complex128")}, "paddle"
)
@to_ivy_arrays_and_back
def not_equal(x, y, /, *, name=None):
    return ivy.not_equal(x, y)


@with_unsupported_dtypes(
    {
        "2.4.2 and below": (
            "uint8",
            "int8",
            "int16",
            "float16",
            "complex64",
            "complex128",
        )
    },
    "paddle",
)
@to_ivy_arrays_and_back
def equal_all(x, y, /, *, name=None):
    return paddle.to_tensor([ivy.array_equal(x, y)])


@with_unsupported_dtypes(
    {"2.4.2 and below": ("bool", "uint8", "int8", "int16", "complex64", "complex128")},
    "paddle",
)
@to_ivy_arrays_and_back
def greater_than(x, y, /, *, name=None):
    return ivy.greater(x, y)


@with_unsupported_dtypes(
    {"2.4.2 and below": ("bool", "uint8", "int8", "int16", "complex64", "complex128")},
    "paddle",
)
@to_ivy_arrays_and_back
def greater_equal(x, y, /, *, name=None):
    return ivy.greater_equal(x, y)


@with_unsupported_dtypes(
    {"2.4.2 and below": ("bool", "uint8", "int8", "int16", "complex64", "complex128")},
    "paddle",
)
@to_ivy_arrays_and_back
def less_than(x, y, /, *, name=None):
    return ivy.less(x, y)


@with_unsupported_dtypes(
    {"2.4.2 and below": ("bool", "uint8", "int8", "int16", "complex64", "complex128")},
    "paddle",
)
@to_ivy_arrays_and_back
def less_equal(x, y, /, *, name=None):
    return ivy.less_equal(x, y)


@with_supported_dtypes(
    {
        "2.4.2 and below": (
            "bool",
            "int8",
            "int16",
            "int32",
            "int64",
            "float32",
            "float64",
        )
    },
    "paddle",
)
@to_ivy_arrays_and_back
@handle_out_argument
def logical_or(x, y, /, *, name=None, out=None):
    return ivy.logical_or(x, y, out=out)


@with_supported_dtypes(
    {
        "2.4.2 and below": (
            "bool",
            "int8",
            "int16",
            "int32",
            "int64",
            "float32",
            "float64",
        )
    },
    "paddle",
)
@to_ivy_arrays_and_back
@handle_out_argument
def logical_xor(x, y, /, *, name=None, out=None):
    return ivy.logical_xor(x, y, out=out)


@with_supported_dtypes(
    {
        "2.4.2 and below": (
            "bool",
            "int8",
            "int16",
            "int32",
            "int64",
            "float32",
            "float64",
        )
    },
    "paddle",
)
@to_ivy_arrays_and_back
@handle_out_argument
def logical_not(x, /, *, name=None, out=None):
    return ivy.logical_not(x, out=out)


@with_supported_dtypes(
    {
        "2.4.2 and below": (
            "bool",
            "uint8",
            "int8",
            "int16",
            "int32",
            "int64",
        )
    },
    "paddle",
)
@to_ivy_arrays_and_back
@handle_out_argument
def bitwise_or(x, y, name=None, out=None):
    return ivy.bitwise_or(x, y, out=out)


@with_supported_dtypes(
    {
        "2.4.2 and below": (
            "bool",
            "uint8",
            "int8",
            "int16",
            "int32",
            "int64",
        )
    },
    "paddle",
)
@to_ivy_arrays_and_back
@handle_out_argument
def bitwise_and(x, y, /, *, name=None, out=None):
    return ivy.bitwise_and(x, y, out=out)
