# frozen_string_literal: true

require_relative "commons/types/Imported"
require "json"

module SeedClient
  module Foo
    class ImportingType
      attr_reader :imported, :additional_properties

      # @param imported [Commons::Imported]
      # @param additional_properties [OpenStruct] Additional properties unmapped to the current class definition
      # @return [Foo::ImportingType]
      def initialze(imported:, additional_properties: nil)
        # @type [Commons::Imported]
        @imported = imported
        # @type [OpenStruct] Additional properties unmapped to the current class definition
        @additional_properties = additional_properties
      end

      # Deserialize a JSON object to an instance of ImportingType
      #
      # @param json_object [JSON]
      # @return [Foo::ImportingType]
      def self.from_json(json_object:)
        struct = JSON.parse(json_object, object_class: OpenStruct)
        imported Commons::Imported.from_json(json_object: struct.imported)
        new(imported: imported, additional_properties: struct)
      end

      # Serialize an instance of ImportingType to a JSON object
      #
      # @return [JSON]
      def to_json(*_args)
        { imported: @imported }.to_json
      end

      # Leveraged for Union-type generation, validate_raw attempts to parse the given hash and check each fields type against the current object's property definitions.
      #
      # @param obj [Object]
      # @return [Void]
      def self.validate_raw(obj:)
        Imported.validate_raw(obj: obj.imported)
      end
    end
  end
end
