require 'json'


MyApp.add_route('POST', '//owners', {
  "resourcePath" => "/OwnerResource",
  "summary" => "createOwner",
  "nickname" => "create_owner_using_post", 
  "responseClass" => "void", 
  "endpoint" => "/owners", 
  "notes" => "",
  "parameters" => [
    {
      "name" => "body",
      "description" => "owner",
      "dataType" => "Owner",
      "paramType" => "body",
    }
    ]}) do
  cross_origin
  # the guts live here

  {"message" => "yes, it worked"}.to_json
end


MyApp.add_route('GET', '//owners', {
  "resourcePath" => "/OwnerResource",
  "summary" => "findAll",
  "nickname" => "find_all_using_get", 
  "responseClass" => "array[Owner]", 
  "endpoint" => "/owners", 
  "notes" => "",
  "parameters" => [
    ]}) do
  cross_origin
  # the guts live here

  {"message" => "yes, it worked"}.to_json
end


MyApp.add_route('GET', '//owners/{ownerId}', {
  "resourcePath" => "/OwnerResource",
  "summary" => "findOwner",
  "nickname" => "find_owner_using_get", 
  "responseClass" => "Owner", 
  "endpoint" => "/owners/{ownerId}", 
  "notes" => "",
  "parameters" => [
    {
      "name" => "owner_id",
      "description" => "ownerId",
      "dataType" => "int",
      "paramType" => "path",
    },
    ]}) do
  cross_origin
  # the guts live here

  {"message" => "yes, it worked"}.to_json
end


MyApp.add_route('PUT', '//owners/{ownerId}', {
  "resourcePath" => "/OwnerResource",
  "summary" => "updateOwner",
  "nickname" => "update_owner_using_put", 
  "responseClass" => "Owner", 
  "endpoint" => "/owners/{ownerId}", 
  "notes" => "",
  "parameters" => [
    {
      "name" => "owner_id",
      "description" => "ownerId",
      "dataType" => "int",
      "paramType" => "path",
    },
    {
      "name" => "body",
      "description" => "ownerRequest",
      "dataType" => "Owner",
      "paramType" => "body",
    }
    ]}) do
  cross_origin
  # the guts live here

  {"message" => "yes, it worked"}.to_json
end

