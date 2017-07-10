#include <iostream>
#include <sstream>
#include <string>
#include "cpprest/containerstream.h"
#include "cpprest/filestream.h"
#include "cpprest/http_client.h"
#include "cpprest/json.h"
#include "cpprest/producerconsumerstream.h"
#include "cpprest/http_client.h"
#include <string.h>
#include <http_client.h>

using namespace std;
using namespace web;
using namespace web::json;
using namespace web::http;
using namespace web::http::client;
using namespace utility;
using namespace utility::conversions;


int main() {

  http_client client(L"http://httpbin.org/ip");

  client.request(methods::GET).then([](http_response response)
  { 
    if(response.status_code() == status_codes::OK)
    {
      auto body = response.extract_string().get();    
      std::cout << body;
    }
  });


  return 0;
}
