#include <base.hpp>
TTY *out;
PMM *pmm;
bool tty_set = false;
void setMainTTY(TTY *obj) {
    ++*obj;
    //        if(tty_set)
    //            --*out;
    out = obj;
    tty_set = true;
}
