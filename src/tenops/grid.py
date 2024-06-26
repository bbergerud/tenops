from typing import Iterable, Union

from .manage import (
    DEFAULT_MODULE,
    TYPEHINT_DTYPE,
    TYPEHINT_MODULE,
    cast_to_dtype,
    get_module_attr,
    get_module_from_object,
    get_module_from_objects,
)
from .utils import AttrHandler, ParameterHandler


def arange(
    *args: int, default: TYPEHINT_MODULE = DEFAULT_MODULE, **kwargs
) -> TYPEHINT_DTYPE:
    a = AttrHandler("arange", tensorflow="range")
    return get_module_attr(default, a[default])(*args, **kwargs)


def cat(
    x: Iterable[TYPEHINT_DTYPE],
    default: TYPEHINT_MODULE = DEFAULT_MODULE,
    axis: int = 0,
    **kwargs
) -> TYPEHINT_DTYPE:
    a = AttrHandler("concat", numpy="concatenate")
    p = ParameterHandler(params={"axis": axis}, axis={"torch": "dim"})
    module = get_module_from_objects(x, default=default)
    x = [cast_to_dtype(xi, module=module) for xi in x]
    return get_module_attr(module, a[module])(x, **p[module], **kwargs)


def empty_like(
    x: TYPEHINT_DTYPE, default: TYPEHINT_MODULE = DEFAULT_MODULE, **kwargs
) -> TYPEHINT_DTYPE:
    a = AttrHandler("empty_like", tensorflow="experimental.numpy.empty_like")
    module = get_module_from_object(x, default=default)
    x = cast_to_dtype(x, module=module)
    return get_module_attr(module, a[module])(x, **kwargs)


def linspace(
    *args: Union[int, float], default: TYPEHINT_MODULE = DEFAULT_MODULE, **kwargs
) -> TYPEHINT_DTYPE:
    a = AttrHandler("linspace")
    return get_module_attr(default, a[default])(*args, **kwargs)


def meshgrid(
    *x: TYPEHINT_DTYPE,
    indexing: str = "ij",
    default: TYPEHINT_MODULE = DEFAULT_MODULE,
    **kwargs
) -> tuple[TYPEHINT_DTYPE]:
    a = AttrHandler("meshgrid")
    p = ParameterHandler(params={"indexing": indexing})
    module = get_module_from_objects(x, default=default)
    x = [cast_to_dtype(xi, module=module) for xi in x]
    return get_module_attr(module, a[module])(*x, **p[module], **kwargs)


def reshape(
    x: TYPEHINT_DTYPE,
    shape: Iterable[int],
    default: TYPEHINT_MODULE = DEFAULT_MODULE,
    **kwargs
) -> TYPEHINT_DTYPE:
    a = AttrHandler("reshape")
    p = ParameterHandler(params={"shape": shape}, shape={"numpy": "newshape"})
    module = get_module_from_object(x, default=default)
    x = cast_to_dtype(x, module=module)
    return get_module_attr(module, a[module])(x, **p[module], **kwargs)


def stack(
    x: Iterable[TYPEHINT_DTYPE],
    default: TYPEHINT_MODULE = DEFAULT_MODULE,
    axis: int = 0,
    **kwargs
) -> TYPEHINT_DTYPE:
    a = AttrHandler("stack")
    p = ParameterHandler(params={"axis": axis}, axis={"torch": "dim"})
    module = get_module_from_objects(x, default=default)
    x = [cast_to_dtype(xi, module=module) for xi in x]
    return get_module_attr(module, a[module])(x, **p[module], **kwargs)


def zeros_like(
    x: TYPEHINT_DTYPE, default: TYPEHINT_MODULE = DEFAULT_MODULE, **kwargs
) -> TYPEHINT_DTYPE:
    a = AttrHandler("zeros_like")
    module = get_module_from_object(x, default=default)
    x = cast_to_dtype(x, module=module)
    return get_module_attr(module, a[module])(x, **kwargs)


# Alias
concat = cat
concatenate = cat
