SUBDIRS = $(shell ls -d */)
CLEAN_TARGETS = $(SUBDIRS:%=clean-%)
UPDATE_TARGETS = $(SUBDIRS:%=update-%)

.PHONY: all clean update $(SUBDIRS) $(CLEAN_TARGETS) $(UPDATE_TARGETS)

all: $(SUBDIRS)

clean: $(CLEAN_TARGETS)

update: $(UPDATE_TARGETS)

$(SUBDIRS):
	$(MAKE) -C $@

$(CLEAN_TARGETS):
	$(MAKE) -C $(@:clean-%=%) clean

$(UPDATE_TARGETS):
	$(MAKE) -C $(@:update-%=%) update
