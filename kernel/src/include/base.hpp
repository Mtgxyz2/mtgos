#pragma once
#include <kobject.hpp>
#include <tty.hpp>
extern TTY *out; ///< main TTY for output
/***
 * Sets the main TTY to some other TTY object.
 */
void setMainTTY(TTY *obj);

/**
 * Halts the kernel due to a unresolvable error
 */
extern "C" void panic(const char* s);

#if !defined(__LITTLE_ENDIAN__) || !defined(__BIG_ENDIAN__)
#if __BYTE_ORDER__ == __ORDER_LITTLE_ENDIAN__
#define __LITTLE_ENDIAN__
#else
#define __BIG_ENDIAN__
#endif
#endif
