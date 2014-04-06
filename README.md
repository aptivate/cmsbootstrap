# cmsbootstrap

Django-CMS basic theme with Bootstrap to get you started quickly.

## Purpose

Django-CMS is very powerful, but comes with no themes by default.
[They say](https://groups.google.com/d/msg/django-cms/4oxF9goRk2g/WEPLSk7OzdYJ):

> Themes are outside the django CMS scope. If you wish to theme the admin,
> just override the template `admin/base_site.html` and include some custom css.

That's all very well, but everyone wanting to start a new project with
Django-CMS faces a lot of study, effort and difficult choices just to get
their first pages to display sensibly. This is where we can help.

## Philosophy

CMS Bootstrap aims to:

### Work with Django-CMS

Themes for non-CMS projects are out of scope.

### Work out of the box

Provide a reasonable basic theme for a Django-CMS site automatically,
out of the box, with no effort.

### Use Bootstrap

Use the Bootstrap project to provide a sensible default theme (toolkit)
that you can pull bits from when you need them, without getting in your way.

### Be reasonably extensible

Make the simple things simple, and the hard things possible. Changing
colours, fonts and sizes should be easy with SCSS.

To that end, we use the
[Sass/SCSS version of Bootstrap](http://getbootstrap.com/getting-started/#download-sass)
so that you can quickly enable and disable modules and change colours.

### Be lightweight

Low bandwidth accessibility is a big part of our philosophy, and this theme
needs to support that. Using Bootstrap/Sass enables us to enable and disable
Bootstrap modules quickly, so we can skip large chunks of CSS and keep the
overall page weight small, while still being flexible.

Our goal on our first project is to keep our pages below 100 kB compressed,
including images, CSS and javascript. This allows them to be loaded within
10 seconds on an 80 kbps connection. Standard Bootstrap CSS alone is 99 kB
(bootstrap-3.1.1-dist/css/bootstrap.min.css), which leaves no room for anything
else on the page within our budget!

### Be reusable

This is related to being extensible, but often in conflict. For example:

To be extensible, a theme needs a lot of hooks to override in subclasses:
Django template blocks, CSS classes applied to elements, etc. But all the
hooks that you're not using are noise that clutters and bloats your pages,
so a page full of hooks is a poor template to copy and modify in your own
code, at least not without ripping out a lot of code.

So our aim is to have *likely* extension points, but not *every possible*
one. Other reuse mechanisms such as:

* Importing existing files wholesale
* Extending (importing and then overriding) existing files
* Reusing a block's contents, but adding to it
* Replacing a file completely
* Disabling a file

should all be supported and used where possible in preference to cluttering
every template with every possible extension point.

### Be maintainable

For the same reason, our "API" to developers should be clear, simple, and
stable: unlikely to change, or need to be changed in future to support newer
versions of Django, Django-CMS, Bootstrap, etc.

### Be portable

As well as slow and unreliable connections, our philosophy is that websites
should be accessible:

* Using old browsers (e.g. Internet Explorer 8) for those without bandwidth,
  skills or permission to upgrade their browsers.
* Using mobile devices (smart phones, feature phones, low cost tablets) as well
  as desktop PCs. So our designs should be responsive, compatible with
  older and simpler browsers such as Opera Mini, and not require Javascript.
* Using free software (Linux, Firefox, Chromium etc.) as well as Windows,
  Internet Explorer and Flash, to access our websites.
* By people using assistive technology (screen readers etc.)
* Into the future, by using web standards properly. So we use HTML5 elements
  such as `header` and `nav` elements, and add backwards compatibility in
  IE8 using Javascript.

Where these standard conflict, we aim to support the largest possible number
of users in our target audience.

### Use Django-Assets

We use [django-assets](https://github.com/miracle2k/django-assets) to
automatically compile Sass/SCSS to standard, minified CSS. It will make your
life better, so we think you should use it too.

You can manually compile the Sass files to standard CSS if you really want to.

## Usage

### With DYE

If you don't yet have a Django-CMS project, the easiest way to get started is:

* [use DYE and cookiecutter](https://github.com/aptivate/dye/blob/develop/readme-cookiecutter.rst)
  to create one,
* enter `cms` for the *Project type*.

Whether this is a new or an existing DYE project, add `cmsbootstrap` to it:

* add this line to `deploy/pip_packages.txt`:
    -e git+https://github.com/aptivate/cmsbootstrap.git
* run `deploy/bootstrap.py`,
* run `deploy/tasks.py deploy:dev`.

### Manual Installation

If you're not using DYE, then install `cmsbootstrap` in your global Python
environment or virtualenv:

    pip install cmsbootstrap

Or if it's not available on PyPI, or you need a newer version:

    pip install -e git+https://github.com/aptivate/cmsbootstrap.git

Of course you need [Django](https://www.djangoproject.com/)
(1.5 or higher) and
[Django-CMS](https://www.django-cms.org/en/) (2.4 or higher) in your
environment as well. They'll be installed automatically by Pip if you don't
have them already.

### Add to `INSTALLED_APPS`

Add `cmsbootstrap` to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'cmsbootstrap',
    )

This allows Django to find the templates and static files that we've provided.
It also allows `django-assets` to find the assets and compile them.

### Building the assets

You'll have to build the assets (CSS files) from the Sass sources at least
once:

    django/website/manage.py assets build

Or you can run the following command, in a spare terminal, to watch the sources
for changes and rebuild them automatically when necessary:

    django/website/manage.py assets watch

### Starting your site

You need some Django-CMS pages to see the templates. If you don't have any,
then you'll just see the Django-CMS pony when you visit your site at
http://localhost:8000/.

Creating pages is not really in the scope of this documentation. But if you
just want to get started quickly, you can 

If you don't have one already, you'll need a superuser to log into the
Django-CMS admin. You can create one like this:

    django/website/manage.py createsuperuser

And run the development server (in a spare terminal):

    django/website/manage.py runserver

You should be able to access http://localhost:8000/ and see the Django-CMS pony.

### Check that the site loads


###



    pip install -e git+https://github.com/aptivate/cmsbootstrap.git

://www.djangoproject.com/









.
./.git
./.git/refs
./.git/refs/heads
./.git/refs/heads/master
./.git/refs/tags
./.git/refs/remotes
./.git/refs/remotes/origin
./.git/refs/remotes/origin/master
./.git/refs/remotes/aptivate
./.git/refs/remotes/aptivate/master
./.git/branches
./.git/hooks
./.git/hooks/commit-msg.sample
./.git/hooks/post-update.sample
./.git/hooks/pre-applypatch.sample
./.git/hooks/pre-commit.sample
./.git/hooks/pre-rebase.sample
./.git/hooks/prepare-commit-msg.sample
./.git/hooks/update.sample
./.git/hooks/applypatch-msg.sample
./.git/info
./.git/info/exclude
./.git/description
./.git/objects
./.git/objects/pack
./.git/objects/info
./.git/objects/5a
./.git/objects/5a/c9288df98a9eb64f961daa9542f3705a0c4ae6
./.git/objects/5a/d22cd6d540fa378940c97910eabad478b09cba
./.git/objects/71
./.git/objects/71/8780467c9ab6b3d8172c6c4ed4ac58d8882736
./.git/objects/71/a836239075aa6e6e4ecb700e9c42c95c022d91
./.git/objects/71/30282b08532c112e461d6abda8b18064544c98
./.git/objects/62
./.git/objects/62/960bb5b27abf1a567a2741c6753f80f31f4136
./.git/objects/62/ce30fa374f8c997c10c000a61a82d1602f2c50
./.git/objects/44
./.git/objects/44/dc634b0ee6356ed1e01e3efc5bce25a1f176f9
./.git/objects/44/8cebd79e723cefaffcd75f2b2f693e352361f8
./.git/objects/44/c12226b0da61ccbddde1b12b43aec22df41754
./.git/objects/22
./.git/objects/22/fbe5dbacbe58748f688cac277d917aebb467b4
./.git/objects/43
./.git/objects/43/6bd2ebcf4831b206383f51b0697ec5075a6930
./.git/objects/43/d7ae3ea4d20db729ec8889539c284ae36714a9
./.git/objects/43/46c865c5e03118b8cad78c5cfae02d7cde2f05
./.git/objects/4c
./.git/objects/4c/42a3b04de277b3d26c3faf3a5b3c49a2752bda
./.git/objects/4c/9546b9beaf6777c982a684c13487f8266aa8ca
./.git/objects/e6
./.git/objects/e6/9de29bb2d1d6434b8b29ae775ad8c2e48c5391
./.git/objects/c4
./.git/objects/c4/ba9696cf96c3e28db96d76ce338bd001ce632f
./.git/objects/89
./.git/objects/89/84b90517fcc5c0b669458b704f7c5b9e23f148
./.git/objects/89/536160990a07218788a41b18aa912c13b093ae
./.git/objects/89/a63dbd9fc53da3a7aa34e9813f4470465690cc
./.git/objects/89/276e49267eca80108225e411771ace4f2a4a1b
./.git/objects/a8
./.git/objects/a8/36b9191f602458741e5b1b606bca3a38e6a1e8
./.git/objects/73
./.git/objects/73/dcfb89a9e08d3e9616c43ddd219c8f96d9802f
./.git/objects/73/02b729d5b426d529711c73f6510722c5442e64
./.git/objects/b8
./.git/objects/b8/a1cceff8f649cdc28d205fd09ad9021fc778ba
./.git/objects/b8/657118a661cfb1f6119f7dccb169db06e4cd04
./.git/objects/76
./.git/objects/76/1ed8ff9d3393be33e6c8abaf3452eddf343c57
./.git/objects/76/6a52462a5ad4adcbc6848f3cbaf764688506b6
./.git/objects/76/8c2347e1b11c103c2a59ad14ab4071dd58ca3a
./.git/objects/ac
./.git/objects/ac/b656d818bf3a3dfe01181674b77607a5413e9f
./.git/objects/59
./.git/objects/59/2bb0f84dc5f76878f8be205837e455b9a27b0d
./.git/objects/59/6d203219e298282502d020d1dd33927ff7c528
./.git/objects/4b
./.git/objects/4b/5c60d97c03943bfe44f6d7c642d06ced7fa028
./.git/objects/05
./.git/objects/05/c909e16c9fa278d8c7af034b23f8d850240bdf
./.git/objects/51
./.git/objects/51/6fe4ff582b0235e8e1665548529464dc10cdfe
./.git/objects/51/cbe85254929af8fd49313f8a53a5e2fdab1347
./.git/objects/51/4c3a00cd8fe49d5846fc81aca72e5501f5fdca
./.git/objects/f4
./.git/objects/f4/d8d8b3089bd6cd3a850993e26dae4f0bf50641
./.git/objects/f4/f317732cba3dccf76632acfbb56bced679edc4
./.git/objects/19
./.git/objects/19/e9af1ed969c7ce8efe8f619990615a3e673c6d
./.git/objects/20
./.git/objects/20/ff270466adc8a66aa6e16dcabdfed090b1a8ee
./.git/objects/23
./.git/objects/23/aa829879fdfcc10444c1c979c9090e4932e84e
./.git/objects/40
./.git/objects/40/0cb7b841e6720bc5ffbd589972f441a2d8d51a
./.git/objects/40/14a80bd4e50de0f1df578cdaf527018cfe3917
./.git/objects/f6
./.git/objects/f6/c0a376c8faa5180e7d30a83ab826cecb79f427
./.git/objects/ef
./.git/objects/ef/a8c17165f893d0ff48cd64fb0bd27923c30f22
./.git/objects/b7
./.git/objects/b7/890d15bfe57c14eec9d3a99113583be10a0996
./.git/objects/80
./.git/objects/80/a7b69dcce544dfa87ae851d92acdae0e93fb0f
./.git/objects/80/42a68660fe6b1a4f9fdb50f83e51953f2fdad1
./.git/objects/80/086952ce339b000494a459c11f8f9967a7c5e6
./.git/objects/80/75252c51db52b42f95e688699118c0105f95d8
./.git/objects/3d
./.git/objects/3d/4c46129c1b01aa5d2b27d5bc639b880b0c0caa
./.git/objects/3d/5ed86d05fd5bdeba1d61f3b1faa2c6055d0868
./.git/objects/3a
./.git/objects/3a/de27abf0fd96008d5d4bd6b7b3cf1331dbbef4
./.git/objects/3a/14565261b995f0978522b4b88766f508457e41
./.git/objects/3a/1f25516bbc7565c5a10668cef2d10346eab671
./.git/objects/46
./.git/objects/46/85ac3a9d4354248baada7a258a0cffc5a4237b
./.git/objects/36
./.git/objects/36/41e333b8d3aa5b6faaea5b3a64c0f01f7c8a7c
./.git/objects/36/55d03953ac830ecd86b55f247ea89b19000996
./.git/objects/06
./.git/objects/06/6b4d77d5517bb41fccc7329c4b2fb47fa82cae
./.git/objects/06/bb3eaf62637b57fc0de33ad3e40e8880f6cc9e
./.git/objects/28
./.git/objects/28/110b6519a0d1542f5e37d05f42cc040b378907
./.git/objects/d8
./.git/objects/d8/f236487ca84b128c58a1987d62b7fb8a4024cc
./.git/objects/d8/f7bc2fb3cc571cea5c1fa4ac85253b3a0da5e4
./.git/objects/d8/acaa38635e67249afaf3fa2c789b2b0575b4d1
./.git/objects/86
./.git/objects/86/632fd34a7935d3257892980fd43906145ebf65
./.git/objects/86/c66c0b7957ba206126a03353c47f9a5019a1eb
./.git/objects/86/37e421c628024291038c43e7c94649bc21b539
./.git/objects/52
./.git/objects/52/6be5b84961d8bce2437167644f0bc2411f539a
./.git/objects/26
./.git/objects/26/2823850fe26185cb2e9675ecfa2a94127bd9d9
./.git/objects/c5
./.git/objects/c5/08835e3cfc29e13a31a1e57710e6ae57c4a083
./.git/objects/f7
./.git/objects/f7/1f8b9015bfecf7d3e7afb0a1b9cfc38741f21e
./.git/objects/6c
./.git/objects/6c/26c1dd6babd12a699ac5733d3beec8b721d31d
./.git/objects/4e
./.git/objects/4e/401e7376bfe8f40ef717f6ff2c6ea305802682
./.git/objects/83
./.git/objects/83/53eb1a657ad24030009636c5d78c45921f0984
./.git/objects/b6
./.git/objects/b6/089912f9c6f626688f31544f9cb63a5b8b273d
./.git/objects/b6/033b49601e4cc62ed0babf45e7bbbbc64ee6b4
./.git/objects/74
./.git/objects/74/ccf9f8b61c758346738db50c7431f73682b323
./.git/objects/93
./.git/objects/93/1092cf0bb8347cba35e97ed190b6b8fbe47359
./.git/objects/8a
./.git/objects/8a/d94374b59945a7685cfc7fa628d3dee95722f0
./.git/objects/c6
./.git/objects/c6/90072be82bddbfd5e16dbd69e7cfcc7fc62c98
./.git/objects/02
./.git/objects/02/4e257c1a13532e7d5579b0ea4bb5915d21e4a6
./.git/objects/65
./.git/objects/65/31fe6f89f4140b159be5fefa334f6f078aac93
./.git/objects/0a
./.git/objects/0a/b992541e2860cea3187f96ae5a730845ac3ada
./.git/objects/6d
./.git/objects/6d/6bed5d15dadb97f3f1f4d91447794ee3c79109
./.git/objects/cd
./.git/objects/cd/9348c6e429a5e5ebf5dfa41d5943bf31ae905e
./.git/objects/cf
./.git/objects/cf/020299affe02354bfbef97b7d926946cc2f840
./.git/objects/cf/d73da678743c4da7bfb0db9dc0ff61225ce90b
./.git/objects/cf/8aa6abd39a29c0dd8b3b976d060c0813957109
./.git/objects/1d
./.git/objects/1d/dfb7ab36fc7db2a511a0dddda470ec5ff52956
./.git/objects/de
./.git/objects/de/c674cb40871ec975cd629951a8783d4141ddcd
./.git/objects/7f
./.git/objects/7f/ee043455dbb00ca5e2f1ca43e2988381b288ce
./.git/objects/85
./.git/objects/85/cb62ea7d6632e67916a63ab744b103070b8a12
./.git/objects/f2
./.git/objects/f2/081b74bfab11a172256c730e5c1844aaac01c1
./.git/objects/ab
./.git/objects/ab/7bb9f87d08443e1d7f4ca3a0017085ce102c2c
./.git/objects/ab/b5219e9c363ba2c5e249b9c3e52e99fae04017
./.git/objects/b1
./.git/objects/b1/7617262089bea95b6d9f789a157ac3c46e594a
./.git/objects/b1/4af6d3313e7a5febcf060bc71130f0bb5614f2
./.git/objects/b1/c33a30865bfdead5c27f35cfe4691a1c9aaa29
./.git/objects/f1
./.git/objects/f1/c73be7c737ef1c04468cf4b3e4928d5ea1484a
./.git/objects/3f
./.git/objects/3f/f20a391f7d3eb83c351754ae5e54b1c7ced905
./.git/objects/42
./.git/objects/42/2c12fc1f0ef951696161a263fefbb58c7a8a65
./.git/objects/42/734feb20cfaba2105e77cf7fada061f68189b3
./.git/objects/1e
./.git/objects/1e/17dfd7d345e8afc7be2e4e4c06131d34ecaecd
./.git/objects/1e/0c555ee2d039f288020ce6e779b61949ec75fb
./.git/objects/e3
./.git/objects/e3/5b70f97014ab400505b177ecfb082fe07b77b1
./.git/objects/8e
./.git/objects/8e/f758c13fa6040ffb1688e3c236773294d71282
./.git/objects/11
./.git/objects/11/5ed349da8d331ddb22300f3c667ca9ab5eda75
./.git/objects/50
./.git/objects/50/1deb776c16733b19f3509d86e125df78958261
./.git/objects/60
./.git/objects/60/f00ef0ef347811e7b0c0921b7fda097acd9fcc
./.git/objects/66
./.git/objects/66/130a3a35be9f5d602207392d847fdd9eced420
./.git/objects/5e
./.git/objects/5e/2ee0d261cf6648132dd611792a00b2fe5e3d59
./.git/objects/1b
./.git/objects/1b/5247001adcb6ab54dc65ad636b0271b1d8e2a8
./.git/objects/c3
./.git/objects/c3/e179784aad058b739eb08c2a22631ce82a4ee6
./.git/objects/c3/a5520a2965815d1ba4eea6e196958257f285dc
./.git/objects/dd
./.git/objects/dd/1e253a1ad98fdbf6d5f1e87469ddf9e2803fe2
./.git/objects/dd/e9043d119586b74ff3ef09a57d1d1cdbd8f4f5
./.git/objects/5d
./.git/objects/5d/e2764d371a95b1681ff5deca6816b44f0763dc
./.git/objects/24
./.git/objects/24/a73ebea2829149ccb050d64b146a644c58a927
./.git/objects/24/13da2a8634d87f83736bb817e2810f5d9b8828
./.git/objects/8c
./.git/objects/8c/cdf4ee177ca396735e82381dc45d6aa67d201b
./.git/objects/04
./.git/objects/04/810fb5b6ed079a0868acad3bdd66fd9ef344bb
./.git/objects/f9
./.git/objects/f9/9af4a61e1bf3b73ae8d033b20b84050291e2d1
./.git/objects/1c
./.git/objects/1c/00307a7519892df1d94f628de7539831bb9db1
./.git/objects/ec
./.git/objects/ec/7ad93dc08d2a798920d501ab33917f27cec113
./.git/objects/45
./.git/objects/45/17bf34621cc1bede82e61c0899e502b77f384c
./.git/objects/fd
./.git/objects/fd/00cd7a715315347cc6bdd0d2ae49bfc70dd884
./.git/objects/16
./.git/objects/16/f6cac44aff9dc9496b88d024b3c0814615578a
./.git/objects/af
./.git/objects/af/322146267792f0fbdb01c32d08142fba4ee412
./.git/objects/14
./.git/objects/14/ee9f75e164e002a22fe88dfe8649e3ff885c10
./.git/objects/b3
./.git/objects/b3/b6b9ded74c999c6909ffb2766ba3c48d8134e7
./.git/objects/88
./.git/objects/88/331b347414d1c74fffbf968a10920a723c9772
./.git/objects/88/bfe56e7e23ce07f5e087c2764fe146c91a48d4
./.git/objects/63
./.git/objects/63/e998d3d525a7c7d73543ccf44ffda6d6e26a98
./.git/objects/b9
./.git/objects/b9/b0d3b9169c57039a0ab3c1a87ecec154b5a9c7
./.git/objects/b9/6f3f55ab6575f8bd2f9fdbc1d3f3372f563d1b
./.git/objects/7c
./.git/objects/7c/cb4ac043c8eb8b46e162f64dd7ff7af313d39d
./.git/objects/03
./.git/objects/03/418bc1b8ef3fd6cadcfee48bf877d017ac5b52
./.git/objects/37
./.git/objects/37/e61365ea319d31083c961cfc06fff3f7ddc8dc
./.git/objects/9a
./.git/objects/9a/706216c343dac6cdb47d645a523f2af4ad3ff5
./.git/objects/84
./.git/objects/84/6e5cbf158e8d200528b1b0588e7df06be3fcaf
./.git/objects/e7
./.git/objects/e7/cab82b3537c8eef4332da5730a59d0867856e7
./.git/objects/67
./.git/objects/67/db875b970ccf4360facb5551addca0da578a58
./.git/objects/ed
./.git/objects/ed/628894d5c08ec5e1fad8547616fe7b18b74b26
./.git/objects/7e
./.git/objects/7e/99fa8aa35d47e78332282ae1df1a86e1813310
./.git/objects/d4
./.git/objects/d4/41c684249783f2ee797bd84f3bde8187651711
./.git/objects/4f
./.git/objects/4f/f7802a8bfd1f4a0126838a8030b58b7428873b
./.git/objects/2c
./.git/objects/2c/cf433e101ec9e7eef7ccc4a6c16cc8c5eb59f6
./.git/objects/f0
./.git/objects/f0/0b36beabdbce89da82b31c3ff392ed0c340a3a
./.git/objects/a7
./.git/objects/a7/d29b61a24a590bd160d380578e408005342430
./.git/objects/98
./.git/objects/98/bc29b6b4ba3ea54992ab443cdde02eb6fcbc7b
./.git/objects/1a
./.git/objects/1a/2a53fb9001d24686fe4b2302629445cc0cbcfa
./.git/objects/e9
./.git/objects/e9/f84df62ab7c4186c0c096dde964b0ac6ef99d8
./.git/objects/49
./.git/objects/49/2a8391b8834924e4312459e79e1b96d4a45dda
./.git/objects/49/8c6b03dee93d515f0bb70c9ee87c02508e0ecb
./.git/objects/0e
./.git/objects/0e/15767bdf95c7a4d78da02748c6b385f058194b
./.git/objects/9d
./.git/objects/9d/fabc69a88cb9da359660027914693d981d79de
./.git/objects/b2
./.git/objects/b2/2434039c1b5f9b718e04000672fb8b42574ee3
./.git/objects/0c
./.git/objects/0c/47266e999518a971e7bb0df22112ab645a60fe
./.git/objects/5c
./.git/objects/5c/919a65a37ae7f2a7e905dff295b3ae55c9dc68
./.git/objects/87
./.git/objects/87/b5d6ab8e0cbd21b11f333ebe131ecbc0461767
./.git/objects/aa
./.git/objects/aa/c0a7ac63c4651ef7e2837aaa63baf4e0b09f21
./.git/objects/ff
./.git/objects/ff/8ef81e9841de96673e6ab2cf87003c81b9b7fa
./.git/objects/64
./.git/objects/64/5d167089ff22bb64edd4eba44b20bcc9e4e05e
./.git/HEAD
./.git/config
./.git/logs
./.git/logs/refs
./.git/logs/refs/heads
./.git/logs/refs/heads/master
./.git/logs/refs/remotes
./.git/logs/refs/remotes/origin
./.git/logs/refs/remotes/origin/master
./.git/logs/refs/remotes/aptivate
./.git/logs/refs/remotes/aptivate/master
./.git/logs/HEAD
./.git/packed-refs
./.git/FETCH_HEAD
./.git/index
./.git/ORIG_HEAD
./.git/COMMIT_EDITMSG
./.gitignore
./LICENSE
./README.md
./cmsbootstrap
./cmsbootstrap/__init__.py
./cmsbootstrap/assets.py
./cmsbootstrap/models.py
./cmsbootstrap/static
./cmsbootstrap/static/bootstrap-sass-3.1.1.tar.gz
./cmsbootstrap/static/css
./cmsbootstrap/static/css/cmsbootstrap
./cmsbootstrap/static/css/cmsbootstrap/ie7.css
./cmsbootstrap/static/css/cmsbootstrap/ie8.css
./cmsbootstrap/static/css/cmsbootstrap/.ie8.css.swp
./cmsbootstrap/static/js
./cmsbootstrap/static/js/bootstrap.js
./cmsbootstrap/static/js/bootstrap
./cmsbootstrap/static/js/bootstrap/affix.js
./cmsbootstrap/static/js/bootstrap/alert.js
./cmsbootstrap/static/js/bootstrap/button.js
./cmsbootstrap/static/js/bootstrap/carousel.js
./cmsbootstrap/static/js/bootstrap/collapse.js
./cmsbootstrap/static/js/bootstrap/dropdown.js
./cmsbootstrap/static/js/bootstrap/modal.js
./cmsbootstrap/static/js/bootstrap/popover.js
./cmsbootstrap/static/js/bootstrap/scrollspy.js
./cmsbootstrap/static/js/bootstrap/tab.js
./cmsbootstrap/static/js/bootstrap/tooltip.js
./cmsbootstrap/static/js/bootstrap/transition.js
./cmsbootstrap/static/js/html5shiv.js
./cmsbootstrap/static/js/lte-ie7.js
./cmsbootstrap/static/js/respond.min.js
./cmsbootstrap/static/sass
./cmsbootstrap/static/sass/bootstrap
./cmsbootstrap/static/sass/bootstrap/_alerts.scss
./cmsbootstrap/static/sass/bootstrap/_badges.scss
./cmsbootstrap/static/sass/bootstrap/_breadcrumbs.scss
./cmsbootstrap/static/sass/bootstrap/_button-groups.scss
./cmsbootstrap/static/sass/bootstrap/_buttons.scss
./cmsbootstrap/static/sass/bootstrap/_carousel.scss
./cmsbootstrap/static/sass/bootstrap/_close.scss
./cmsbootstrap/static/sass/bootstrap/_code.scss
./cmsbootstrap/static/sass/bootstrap/_component-animations.scss
./cmsbootstrap/static/sass/bootstrap/_dropdowns.scss
./cmsbootstrap/static/sass/bootstrap/_forms.scss
./cmsbootstrap/static/sass/bootstrap/_glyphicons.scss
./cmsbootstrap/static/sass/bootstrap/_grid.scss
./cmsbootstrap/static/sass/bootstrap/_input-groups.scss
./cmsbootstrap/static/sass/bootstrap/_jumbotron.scss
./cmsbootstrap/static/sass/bootstrap/_labels.scss
./cmsbootstrap/static/sass/bootstrap/_list-group.scss
./cmsbootstrap/static/sass/bootstrap/_media.scss
./cmsbootstrap/static/sass/bootstrap/_mixins.scss
./cmsbootstrap/static/sass/bootstrap/_modals.scss
./cmsbootstrap/static/sass/bootstrap/_navbar.scss
./cmsbootstrap/static/sass/bootstrap/_navs.scss
./cmsbootstrap/static/sass/bootstrap/_normalize.scss
./cmsbootstrap/static/sass/bootstrap/_pager.scss
./cmsbootstrap/static/sass/bootstrap/_pagination.scss
./cmsbootstrap/static/sass/bootstrap/_panels.scss
./cmsbootstrap/static/sass/bootstrap/_popovers.scss
./cmsbootstrap/static/sass/bootstrap/_print.scss
./cmsbootstrap/static/sass/bootstrap/_progress-bars.scss
./cmsbootstrap/static/sass/bootstrap/_responsive-utilities.scss
./cmsbootstrap/static/sass/bootstrap/_scaffolding.scss
./cmsbootstrap/static/sass/bootstrap/_tables.scss
./cmsbootstrap/static/sass/bootstrap/_theme.scss
./cmsbootstrap/static/sass/bootstrap/_thumbnails.scss
./cmsbootstrap/static/sass/bootstrap/_tooltip.scss
./cmsbootstrap/static/sass/bootstrap/_type.scss
./cmsbootstrap/static/sass/bootstrap/_utilities.scss
./cmsbootstrap/static/sass/bootstrap/_variables.scss
./cmsbootstrap/static/sass/bootstrap/_wells.scss
./cmsbootstrap/static/sass/bootstrap/bootstrap.scss
./cmsbootstrap/static/sass/bootstrap/._navbar.scss.swp
./cmsbootstrap/static/sass/bootstrap/._navs.scss.swp
./cmsbootstrap/static/sass/cmsbootstrap.scss
./cmsbootstrap/static/sass/.cmsbootstrap.scss.swp
./cmsbootstrap/templates
./cmsbootstrap/templates/base.html
./cmsbootstrap/templates/cmsbootstrap
./cmsbootstrap/templates/cmsbootstrap/base.html
./cmsbootstrap/templates/cmsbootstrap/homepage.html
./cmsbootstrap/templates/cmsbootstrap/menu
./cmsbootstrap/templates/cmsbootstrap/menu/breadcrumb.html
./cmsbootstrap/templates/cmsbootstrap/menu/language_chooser.html
./cmsbootstrap/templates/cmsbootstrap/menu/menu.html
./cmsbootstrap/templates/cmsbootstrap/menu/.language_chooser.html.swp
./cmsbootstrap/templates/cmsbootstrap/page_3col.html
./cmsbootstrap/templates/cmsbootstrap/page_3col_notitle.html
./cmsbootstrap/templates/cmsbootstrap/placeholders_extra.html
./cmsbootstrap/templates/cmsbootstrap/.base.html.swp
./cmsbootstrap/tests.py
./cmsbootstrap/views.py
./cmsbootstrap/__init__.pyc
./cmsbootstrap/models.pyc
./cmsbootstrap/assets.pyc
./setup.py
./cmsbootstrap.egg-info
./cmsbootstrap.egg-info/requires.txt
./cmsbootstrap.egg-info/PKG-INFO
./cmsbootstrap.egg-info/top_level.txt
./cmsbootstrap.egg-info/dependency_links.txt
./cmsbootstrap.egg-info/SOURCES.txt
