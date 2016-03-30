Name     : rubygem-ethon
Version  : 0.8.1
Release  : 5
URL      : https://rubygems.org/downloads/ethon-0.8.1.gem
Source0  : https://rubygems.org/downloads/ethon-0.8.1.gem
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
%setup -q -D -T -n ethon-0.8.1
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
ethon-0.8.1.gem

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
pushd %{buildroot}%{gem_dir}/gems/ethon-0.8.1
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
/usr/lib64/ruby/gems/2.3.0/cache/ethon-0.8.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/Guardfile
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/README.md
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/ethon.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/curl.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/curls/classes.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/curls/codes.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/curls/constants.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/curls/form_options.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/curls/functions.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/curls/infos.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/curls/messages.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/curls/options.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/curls/settings.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/callbacks.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/debug_info.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/features.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/form.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/header.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/http.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/http/actionable.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/http/custom.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/http/delete.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/http/get.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/http/head.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/http/options.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/http/patch.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/http/post.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/http/postable.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/http/put.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/http/putable.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/informations.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/mirror.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/operations.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/options.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/params.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/queryable.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/response_callbacks.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/easy/util.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/errors.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/errors/ethon_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/errors/global_init.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/errors/invalid_option.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/errors/invalid_value.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/errors/multi_add.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/errors/multi_fdset.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/errors/multi_remove.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/errors/multi_timeout.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/errors/select.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/libc.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/loggable.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/multi.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/multi/operations.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/multi/options.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/multi/stack.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/lib/ethon/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/profile/benchmarks.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/profile/memory_leaks.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/profile/perf_spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/profile/support/memory_test_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/profile/support/os_memory_leak_tracker.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/profile/support/ruby_object_leak_tracker.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/curl_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/callbacks_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/debug_info_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/features_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/form_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/header_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/http/custom_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/http/delete_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/http/get_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/http/head_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/http/options_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/http/patch_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/http/post_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/http/put_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/http_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/informations_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/mirror_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/operations_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/options_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/queryable_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/response_callbacks_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy/util_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/easy_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/libc_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/loggable_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/multi/operations_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/multi/options_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/multi/stack_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/ethon/multi_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/support/localhost_server.rb
/usr/lib64/ruby/gems/2.3.0/gems/ethon-0.8.1/spec/support/server.rb
/usr/lib64/ruby/gems/2.3.0/specifications/ethon-0.8.1.gemspec
