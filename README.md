Gueco-nc
========

## Usage

### Step 1: Create a CLIPS Environment

    var clips = require('gueco-nc');
    var env = new clips.Environment();

### Step 2: Initialize and Run Environment

    env.initialize( function {

      // Load .clp file
      env.load(__dirname+'/animal.clp', function () {

        // Reset environment and run
        env.reset(function(){
          env.run(function() {

            // Log fact list to console
            console.log(env.facts());

            // Dispose of the CLIPS environment and free memory
            env.dispose(function(){

            });
          });
        });
      });
    });

## Environment Methods

### load (filename, callback)
Load the constructs from the specified file into the CLIPS environment.

### save (filename, callback)
Save the constructs in the current environment to a file.

### bload (filename, callback)
Load the constructs from the specified binary file into the CLIPS environment. This is considerably faster than a simple load due to the time saved on parsing the constructs.

### bsave (filename, callback)
Save the constructs in the current environment to a binary file.

### eval (expression, callback)
Evaluate the expression as if it was entered into the CLIPS command line. The ```eval``` function cannot be used to define constructs. To define constructs use the ```build``` function.

### build (expression, callback)
Evaluates the expression as if it was entered into the CLIPS command line. Can be used to define any CLIPS constructs .

### reset (callback)
Reset the CLIPS environment.

### run (callback)
Allows rules to execute.

### clear (callback)

Clears the current CLIPS environment of all constructs.

### assert (fact, callback)

Assert a fact into CLIPS.

### facts (callback)

Get a list of facts.
