// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: Description.proto

#ifndef PROTOBUF_Description_2eproto__INCLUDED
#define PROTOBUF_Description_2eproto__INCLUDED

#include <string>

#include <google/protobuf/stubs/common.h>

#if GOOGLE_PROTOBUF_VERSION < 2005000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please update
#error your headers.
#endif
#if 2005000 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)

namespace promc {

// Internal implementation detail -- do not call these.
void  protobuf_AddDesc_Description_2eproto();
void protobuf_AssignDesc_Description_2eproto();
void protobuf_ShutdownFile_Description_2eproto();

class Description;

// ===================================================================

class Description : public ::google::protobuf::Message {
 public:
  Description();
  virtual ~Description();

  Description(const Description& from);

  inline Description& operator=(const Description& from) {
    CopyFrom(from);
    return *this;
  }

  inline const ::google::protobuf::UnknownFieldSet& unknown_fields() const {
    return _unknown_fields_;
  }

  inline ::google::protobuf::UnknownFieldSet* mutable_unknown_fields() {
    return &_unknown_fields_;
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const Description& default_instance();

  void Swap(Description* other);

  // implements Message ----------------------------------------------

  Description* New() const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const Description& from);
  void MergeFrom(const Description& from);
  void Clear();
  bool IsInitialized() const;

  int ByteSize() const;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input);
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const;
  ::google::protobuf::uint8* SerializeWithCachedSizesToArray(::google::protobuf::uint8* output) const;
  int GetCachedSize() const { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const;
  public:

  ::google::protobuf::Metadata GetMetadata() const;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // required uint64 version = 1;
  inline bool has_version() const;
  inline void clear_version();
  static const int kVersionFieldNumber = 1;
  inline ::google::protobuf::uint64 version() const;
  inline void set_version(::google::protobuf::uint64 value);

  // required uint64 events = 2;
  inline bool has_events() const;
  inline void clear_events();
  static const int kEventsFieldNumber = 2;
  inline ::google::protobuf::uint64 events() const;
  inline void set_events(::google::protobuf::uint64 value);

  // required string description = 3;
  inline bool has_description() const;
  inline void clear_description();
  static const int kDescriptionFieldNumber = 3;
  inline const ::std::string& description() const;
  inline void set_description(const ::std::string& value);
  inline void set_description(const char* value);
  inline void set_description(const char* value, size_t size);
  inline ::std::string* mutable_description();
  inline ::std::string* release_description();
  inline void set_allocated_description(::std::string* description);

  // required uint64 timestamp = 4;
  inline bool has_timestamp() const;
  inline void clear_timestamp();
  static const int kTimestampFieldNumber = 4;
  inline ::google::protobuf::uint64 timestamp() const;
  inline void set_timestamp(::google::protobuf::uint64 value);

  // @@protoc_insertion_point(class_scope:promc.Description)
 private:
  inline void set_has_version();
  inline void clear_has_version();
  inline void set_has_events();
  inline void clear_has_events();
  inline void set_has_description();
  inline void clear_has_description();
  inline void set_has_timestamp();
  inline void clear_has_timestamp();

  ::google::protobuf::UnknownFieldSet _unknown_fields_;

  ::google::protobuf::uint64 version_;
  ::google::protobuf::uint64 events_;
  ::std::string* description_;
  ::google::protobuf::uint64 timestamp_;

  mutable int _cached_size_;
  ::google::protobuf::uint32 _has_bits_[(4 + 31) / 32];

  friend void  protobuf_AddDesc_Description_2eproto();
  friend void protobuf_AssignDesc_Description_2eproto();
  friend void protobuf_ShutdownFile_Description_2eproto();

  void InitAsDefaultInstance();
  static Description* default_instance_;
};
// ===================================================================


// ===================================================================

// Description

// required uint64 version = 1;
inline bool Description::has_version() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void Description::set_has_version() {
  _has_bits_[0] |= 0x00000001u;
}
inline void Description::clear_has_version() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void Description::clear_version() {
  version_ = GOOGLE_ULONGLONG(0);
  clear_has_version();
}
inline ::google::protobuf::uint64 Description::version() const {
  return version_;
}
inline void Description::set_version(::google::protobuf::uint64 value) {
  set_has_version();
  version_ = value;
}

// required uint64 events = 2;
inline bool Description::has_events() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void Description::set_has_events() {
  _has_bits_[0] |= 0x00000002u;
}
inline void Description::clear_has_events() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void Description::clear_events() {
  events_ = GOOGLE_ULONGLONG(0);
  clear_has_events();
}
inline ::google::protobuf::uint64 Description::events() const {
  return events_;
}
inline void Description::set_events(::google::protobuf::uint64 value) {
  set_has_events();
  events_ = value;
}

// required string description = 3;
inline bool Description::has_description() const {
  return (_has_bits_[0] & 0x00000004u) != 0;
}
inline void Description::set_has_description() {
  _has_bits_[0] |= 0x00000004u;
}
inline void Description::clear_has_description() {
  _has_bits_[0] &= ~0x00000004u;
}
inline void Description::clear_description() {
  if (description_ != &::google::protobuf::internal::kEmptyString) {
    description_->clear();
  }
  clear_has_description();
}
inline const ::std::string& Description::description() const {
  return *description_;
}
inline void Description::set_description(const ::std::string& value) {
  set_has_description();
  if (description_ == &::google::protobuf::internal::kEmptyString) {
    description_ = new ::std::string;
  }
  description_->assign(value);
}
inline void Description::set_description(const char* value) {
  set_has_description();
  if (description_ == &::google::protobuf::internal::kEmptyString) {
    description_ = new ::std::string;
  }
  description_->assign(value);
}
inline void Description::set_description(const char* value, size_t size) {
  set_has_description();
  if (description_ == &::google::protobuf::internal::kEmptyString) {
    description_ = new ::std::string;
  }
  description_->assign(reinterpret_cast<const char*>(value), size);
}
inline ::std::string* Description::mutable_description() {
  set_has_description();
  if (description_ == &::google::protobuf::internal::kEmptyString) {
    description_ = new ::std::string;
  }
  return description_;
}
inline ::std::string* Description::release_description() {
  clear_has_description();
  if (description_ == &::google::protobuf::internal::kEmptyString) {
    return NULL;
  } else {
    ::std::string* temp = description_;
    description_ = const_cast< ::std::string*>(&::google::protobuf::internal::kEmptyString);
    return temp;
  }
}
inline void Description::set_allocated_description(::std::string* description) {
  if (description_ != &::google::protobuf::internal::kEmptyString) {
    delete description_;
  }
  if (description) {
    set_has_description();
    description_ = description;
  } else {
    clear_has_description();
    description_ = const_cast< ::std::string*>(&::google::protobuf::internal::kEmptyString);
  }
}

// required uint64 timestamp = 4;
inline bool Description::has_timestamp() const {
  return (_has_bits_[0] & 0x00000008u) != 0;
}
inline void Description::set_has_timestamp() {
  _has_bits_[0] |= 0x00000008u;
}
inline void Description::clear_has_timestamp() {
  _has_bits_[0] &= ~0x00000008u;
}
inline void Description::clear_timestamp() {
  timestamp_ = GOOGLE_ULONGLONG(0);
  clear_has_timestamp();
}
inline ::google::protobuf::uint64 Description::timestamp() const {
  return timestamp_;
}
inline void Description::set_timestamp(::google::protobuf::uint64 value) {
  set_has_timestamp();
  timestamp_ = value;
}


// @@protoc_insertion_point(namespace_scope)

}  // namespace promc

#ifndef SWIG
namespace google {
namespace protobuf {


}  // namespace google
}  // namespace protobuf
#endif  // SWIG

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_Description_2eproto__INCLUDED
