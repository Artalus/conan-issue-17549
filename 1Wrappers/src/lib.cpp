#include <Wrappers.hpp>

bool wrap(rttr::variant &x) {
    return x.is_valid();
}
