Name     : rubygem-ethon
Version  : 0.7.4
Release  : 3
URL      : https://rubygems.org/downloads/ethon-0.7.4.gem
Source0  : https://rubygems.org/downloads/ethon-0.7.4.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-ffi
BuildRequires : rubygem-rack
BuildRequires : rubygem-rack-protection
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-sinatra
BuildRequires : rubygem-tilt

%description
#  Ethon [![Build Status](https://secure.travis-ci.org/typhoeus/ethon.png?branch=master)](http://travis-ci.org/typhoeus/ethon) [![Gem Version](https://badge.fury.io/rb/ethon.png)](http://badge.fury.io/rb/ethon)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n ethon-0.7.4
gem spec %{SOURCE0} -l --ruby > rubygem-ethon.gemspec

%build
gem build rubygem-ethon.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
ethon-0.7.4.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/ethon-0.7.4
# Don't use Bundler.
sed -i -e "/require 'bundler'/ s/^/#/" \
    -e "/Bundler.setup/ s/^/#/" \
    spec/spec_helper.rb

# Triggers NoMethodError
sed -i '/skip/ s/^/#/' spec/ethon/multi/operations_spec.rb

rspec -I.:lib spec/ ||: 
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/ethon-0.7.4.gem
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curl/FDSet/FFI/Type/cdesc-Type.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curl/FDSet/FFI/cdesc-FFI.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curl/FDSet/cdesc-FDSet.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curl/FDSet/clear-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curl/Msg/cdesc-Msg.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curl/MsgData/cdesc-MsgData.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curl/Timeval/cdesc-Timeval.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curl/VersionInfoData/cdesc-VersionInfoData.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curl/cdesc-Curl.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Codes/cdesc-Codes.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Codes/easy_codes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Codes/multi_codes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/FormOptions/cdesc-FormOptions.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/FormOptions/form_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Functions/cdesc-Functions.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Infos/cdesc-Infos.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Infos/debug_info_types-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Infos/double_ptr-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Infos/get_info_double-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Infos/get_info_long-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Infos/get_info_string-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Infos/info_types-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Infos/infos-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Infos/long_ptr-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Infos/string_ptr-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Messages/cdesc-Messages.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Messages/msg_codes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Options/cdesc-Options.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Options/option-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Options/option_alias-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Options/option_type-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/Options/set_option-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Curls/cdesc-Curls.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Callbacks/cdesc-Callbacks.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/DebugInfo/Message/cdesc-Message.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/DebugInfo/Message/message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/DebugInfo/Message/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/DebugInfo/Message/type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/DebugInfo/add-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/DebugInfo/cdesc-DebugInfo.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/DebugInfo/messages_for-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/DebugInfo/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/DebugInfo/to_a-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/DebugInfo/to_h-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Features/cdesc-Features.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Features/supports_asynch_dns%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Features/supports_timeout_ms%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Features/supports_zlib%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Form/cdesc-Form.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Form/first-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Form/form_add-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Form/last-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Form/materialize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Form/multipart%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Form/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Form/setup_garbage_collection-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Header/cdesc-Header.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Header/compose_header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Header/header_list-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Header/headers%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Header/headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Actionable/cdesc-Actionable.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Actionable/form-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Actionable/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Actionable/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Actionable/params-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Actionable/params_encoding-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Actionable/parse_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Actionable/query_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Actionable/set_form-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Actionable/set_params-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Actionable/setup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Actionable/url-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Custom/cdesc-Custom.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Custom/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Custom/setup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Delete/cdesc-Delete.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Delete/setup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Get/cdesc-Get.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Get/setup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Head/cdesc-Head.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Head/setup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Options/cdesc-Options.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Options/setup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Patch/cdesc-Patch.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Patch/setup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Post/cdesc-Post.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Post/setup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Postable/cdesc-Postable.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Postable/set_form-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Put/cdesc-Put.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Put/setup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Putable/cdesc-Putable.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/Putable/set_form-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/cdesc-Http.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/fabricate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Http/http_request-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Informations/cdesc-Informations.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Informations/supports_zlib%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Mirror/cdesc-Mirror.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Mirror/from_easy-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Mirror/informations_to_log-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Mirror/informations_to_mirror-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Mirror/log_informations-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Mirror/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Mirror/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Mirror/to_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Operations/cdesc-Operations.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Operations/handle-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Operations/perform-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Operations/prepare-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Options/cdesc-Options.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Options/url%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Options/url-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Params/cdesc-Params.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Params/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Queryable/cdesc-Queryable.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/ResponseCallbacks/body-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/ResponseCallbacks/cdesc-ResponseCallbacks.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/ResponseCallbacks/complete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/ResponseCallbacks/headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/ResponseCallbacks/on_body-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/ResponseCallbacks/on_complete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/ResponseCallbacks/on_headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Util/cdesc-Util.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/Util/escape_zero_byte-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/cdesc-Easy.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/escape-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/log_inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/mirror-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/reset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/return_code-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/set_attributes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Easy/to_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Errors/EthonError/cdesc-EthonError.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Errors/GlobalInit/cdesc-GlobalInit.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Errors/GlobalInit/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Errors/InvalidOption/cdesc-InvalidOption.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Errors/InvalidOption/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Errors/InvalidValue/cdesc-InvalidValue.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Errors/InvalidValue/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Errors/MultiAdd/cdesc-MultiAdd.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Errors/MultiAdd/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Errors/MultiFdset/cdesc-MultiFdset.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Errors/MultiFdset/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Errors/MultiRemove/cdesc-MultiRemove.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Errors/MultiRemove/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Errors/MultiTimeout/cdesc-MultiTimeout.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Errors/MultiTimeout/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Errors/Select/cdesc-Select.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Errors/Select/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Errors/cdesc-Errors.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Libc/cdesc-Libc.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Loggable/cdesc-Loggable.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Loggable/default_logger-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Loggable/logger%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Loggable/logger-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Loggable/rails_logger-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Operations/cdesc-Operations.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Operations/check-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Operations/get_timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Operations/handle-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Operations/init_vars-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Operations/ongoing%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Operations/perform-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Operations/prepare-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Operations/reset_fds-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Operations/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Operations/running_count-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Operations/set_fds-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Operations/trigger-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Options/cdesc-Options.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Options/max_total_connections%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Options/maxconnects%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Options/pipelining%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Options/socketdata%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Options/socketfunction%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Options/timerdata%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Options/timerfunction%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Options/value_for-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Stack/add-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Stack/cdesc-Stack.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Stack/delete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/Stack/easy_handles-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/cdesc-Multi.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/Multi/set_attributes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/Ethon/cdesc-Ethon.ri
/usr/lib64/ruby/gems/2.2.0/doc/ethon-0.7.4/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/.rspec
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/.travis.yml
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/CHANGELOG.md
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/Guardfile
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/README.md
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/ethon.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/curl.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/curls/classes.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/curls/codes.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/curls/constants.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/curls/form_options.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/curls/functions.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/curls/infos.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/curls/messages.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/curls/options.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/curls/settings.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/callbacks.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/debug_info.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/features.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/form.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/header.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/http.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/http/actionable.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/http/custom.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/http/delete.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/http/get.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/http/head.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/http/options.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/http/patch.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/http/post.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/http/postable.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/http/put.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/http/putable.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/informations.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/mirror.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/operations.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/options.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/params.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/queryable.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/response_callbacks.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/easy/util.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/errors.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/errors/ethon_error.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/errors/global_init.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/errors/invalid_option.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/errors/invalid_value.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/errors/multi_add.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/errors/multi_fdset.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/errors/multi_remove.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/errors/multi_timeout.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/errors/select.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/libc.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/loggable.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/multi.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/multi/operations.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/multi/options.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/multi/stack.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/lib/ethon/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/profile/benchmarks.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/profile/memory_leaks.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/profile/perf_spec_helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/profile/support/memory_test_helpers.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/profile/support/os_memory_leak_tracker.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/profile/support/ruby_object_leak_tracker.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/curl_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/callbacks_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/debug_info_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/features_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/form_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/header_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/http/custom_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/http/delete_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/http/get_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/http/head_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/http/options_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/http/patch_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/http/post_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/http/put_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/http_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/informations_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/mirror_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/operations_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/options_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/queryable_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/response_callbacks_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy/util_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/easy_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/libc_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/loggable_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/multi/operations_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/multi/options_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/multi/stack_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/ethon/multi_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/support/localhost_server.rb
/usr/lib64/ruby/gems/2.2.0/gems/ethon-0.7.4/spec/support/server.rb
/usr/lib64/ruby/gems/2.2.0/specifications/ethon-0.7.4.gemspec
