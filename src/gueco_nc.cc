#include "clips_environment.h"

using namespace v8;

void InitAll(Handle<Object> exports) {
  CLIPSEnvironment::Init(exports);
}

NODE_MODULE(gueco_ns, InitAll)
