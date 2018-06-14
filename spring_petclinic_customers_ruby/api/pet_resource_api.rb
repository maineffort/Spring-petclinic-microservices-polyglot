require 'json'


MyApp.add_route('GET', '//owners/*/pets/{petId}', {
  "resourcePath" => "/PetResource",
  "summary" => "findPet",
  "nickname" => "find_pet_using_get", 
  "responseClass" => "PetDetails", 
  "endpoint" => "/owners/*/pets/{petId}", 
  "notes" => "",
  "parameters" => [
    {
      "name" => "pet_id",
      "description" => "petId",
      "dataType" => "int",
      "paramType" => "path",
    },
    ]}) do
  cross_origin
  # the guts live here

  {"message" => "yes, it worked"}.to_json
end


MyApp.add_route('GET', '//petTypes', {
  "resourcePath" => "/PetResource",
  "summary" => "getPetTypes",
  "nickname" => "get_pet_types_using_get", 
  "responseClass" => "array[PetType]", 
  "endpoint" => "/petTypes", 
  "notes" => "",
  "parameters" => [
    ]}) do
  cross_origin
  # the guts live here

  {"message" => "yes, it worked"}.to_json
end


MyApp.add_route('POST', '//owners/{ownerId}/pets', {
  "resourcePath" => "/PetResource",
  "summary" => "processCreationForm",
  "nickname" => "process_creation_form_using_post", 
  "responseClass" => "void", 
  "endpoint" => "/owners/{ownerId}/pets", 
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
      "description" => "petRequest",
      "dataType" => "PetRequest",
      "paramType" => "body",
    }
    ]}) do
  cross_origin
  # the guts live here

  {"message" => "yes, it worked"}.to_json
end


MyApp.add_route('PUT', '//owners/*/pets/{petId}', {
  "resourcePath" => "/PetResource",
  "summary" => "processUpdateForm",
  "nickname" => "process_update_form_using_put", 
  "responseClass" => "void", 
  "endpoint" => "/owners/*/pets/{petId}", 
  "notes" => "",
  "parameters" => [
    {
      "name" => "body",
      "description" => "petRequest",
      "dataType" => "PetRequest",
      "paramType" => "body",
    }
    ]}) do
  cross_origin
  # the guts live here

  {"message" => "yes, it worked"}.to_json
end

