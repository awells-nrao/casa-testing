# envvar defintion
CURRENT_DIR=$PWD

# alias definitions

export CGUIDES_WORKSPACE=$CURRENT_DIR/workspace
export CGUIDES_EXTRACTED=$CGUIDES_WORKSPACE/extracted
export CGUIDES_REGRESSION=$CGUIDES_WORKSPACE/regression
export CGUIDES_CONFIG=$CURRENT_DIR/config
export CGUIDES_CSPECS=$CURRENT_DIR/templates

# post
mkdir -p $CGUIDES_EXTRACTED
mkdir -p $CGUIDES_REGRESSION

# /home/casa/casaGuideData