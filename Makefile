SUBDIRS = data
CLEAN_TARGETS = $(SUBDIRS:%=clean-%)
UPDATE_TARGETS = $(SUBDIRS:%=update-%)

.PHONY: all clean update $(SUBDIRS) $(CLEAN_TARGETS) $(UPDATE_TARGETS)

all: generate-csvs
	python generate_report.py | cat INTRO.md - > README.md
	$(MAKE) -C graphics
	pandoc README.md -o README.pdf
	
generate-csvs: $(SUBDIRS)

clean: $(CLEAN_TARGETS)
	$(MAKE) -C graphics clean
	rm -f README.md

update: $(UPDATE_TARGETS)

$(SUBDIRS):
	$(MAKE) -C $@

$(CLEAN_TARGETS):
	$(MAKE) -C $(@:clean-%=%) clean

$(UPDATE_TARGETS):
	$(MAKE) -C $(@:update-%=%) update
