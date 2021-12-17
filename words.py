words = [
    (("A mistake in typed code that violates \nthe rules of the programming language."), ("Syntax error")),
    (("A mistake in an algorithm or program that \ncauses it to behave unexpectedly or return the incorrect value."), ("Logic error")),
    (("A mistake in a program that happens only when \nthe program is actually run, such as a program\nattempting to access memory that does not exist."), ("Run time error")),
    (("Error that results when the number of bits\nis not enough to represent the \nnumber(like a car’s odometer “rolling over”)."), ("Overflow error")),
    (("A binary digit, either 0 or 1."), ("Bit")),
    (("A sequence of 8 bits."), ("Byte")),
    (("Error that results when the number of bits\nis not enough to represent the number with full\nprecision (like using 3 digits to represent π as 3.14)."), ("Roundoff")),
    (("Values that change smoothly, rather than in\ndiscrete intervals, over time. For example, the\npitch and volume of a live concert. "), ("Analog data")),
    (("Compressing data in a way that preserves all data\naway and allows full recovery of the original."), ("Lossless")),
    (("Compressing data in a way that discards some data\n and makes it impossible to recover the original."), ("Lossy")),
    (("Data about data, like descriptive information\nabout a file or a row in a database."), ("Metadata")),
    (("The sequential execution of steps in an\nalgorithm or code in a program (like steps in a recipe)."), ("Sequencing")),
    (("A Boolean condition to determine which of\ntwo paths are taken in an algorithm or program."), ("Selection")),
    (("The repetition of steps in an algorithm or program\nfor a certain amount of times or until a certain condition is met."),("Iteration")),
    (("An algorithm that iterates through each item in\na list until it finds the target value."),("Linear search")),
    (("An algorithm that searches a sorted list for a\nvalue by repeatedly splitting the list in half."), ("Binary search")),
    (("A run time for an algorithm that doesn't increase\nfaster than a polynomial function of the input size."), ("Reasonable time")),
    (("A technique that helps an algorithm find\na good solution in a hard problem."), ("Heuristic")),
    (("A problem that is so logically difficult,\nwe can’t ever create an algorithm that\nwould be able to answer yes or no for all inputs."),("Undecidable")),
    (("A collection of procedures that\nare useful in creating programs."),("Library")),
    (("Application Programming Interface, a library\nof procedures and a description of how to\ncall each procedure."),("API")),
    (("The separation of a program into independent\nmodules that are each responsible for\none aspect of the program's functionality."),("Modularity")),
    (("The iteration over the items in a list."),("Traversal")),
    (("A physical device that can run a program,\nsuch as a computer, smart phone, or smart sensor."),("Computing device")),
    (("A group of interconnected computing devices capable\nof sending or receiving data."),("Network")),
    (("The maximum amount of data that can be sent in a \nfixed period of time over a network connection,\ntypically measured in bits per second."),("Bandwidth")),
    (("An agreed upon set of rules that\nspecify the behavior of a system. "),("Protocol")),
    (("The ability of a system to adjust\nin scale to meet new demands. "),("Scalability")),
    (("The protocol that determines how to address nodes\non the network and how to route data from\none node to a destination node."),("Internet protocol")),
    (("A data transport protocol that includes mechanisms for\nreliably transmitting packets to a destination."),("TCP")),
    (("A lightweight data transport protocol\nwith minimal error checking."),("UDP")),
    (("A system of linked pages, media,\nand files, browsable over HTTP."),("World wide web")),
    (("The protocol that powers the Web, used to request\nwebpages from servers and submit form data to servers."),("HTTP")),
    (("A computational model which splits a program into multiple\ntasks, some of which can be executed simultaneously."),("Parallel computing")),
    (("The improvement in the amount of time a parallelized\nprogram takes to solve a problem."),("Speedup")),
    (("A computational model which uses multiple\ndevices to run different parts of a program."),("Distributed computing")),
    (("The idea that some communities or populations\nhave less access to computing than others."),("Digital divide")),
    (("A model in which many online users combine\nefforts to help fund projects,\ngenerate ideas, or create goods or services."),("Crowd sourcing")),
    (("Crowdsourcing for science!\nThe participation of volunteers from the public\nin a scientific research project."),("Citizen science")),
    (("An alternative to copyright that allows people to declare how\nthey want their artistic creations to be shared,\nremixed, used in noncommercial contexts"),("Creative commons")),
    (("A policy that allows people to have access to documents\n(like research papers) for reading or data\n(like government datasets) for analysis."),("Open access")),
    (("Information about an individual that can\nbe used to uniquely identify them,\ndirectly or indirectly."),("Personally identifiable information")),
    (("A method of user authentication which requires the\nuser to present multiple pieces of evidence\nin multiple categories."),("Multifactor authentication")),
    (("The process of scrambling data\nto prevent unauthorized access."),("Encryption")),
    (("A technique for encrypting data where the same\nkey is used to both encrypt and decrypt data."),("Symmetric encryption")),
    (("An asymmetric encryption technique that uses different\nkeys for encrypting versus decrypting data."),("Public key encryption")),
    (("A small amount of text that tracks information about a user visiting a website."),("Cookie")),
    (("A type of computer malware that\ncan make copies of itself."),("Virus")),
    (("An attack where a user is tricked\ninto revealing private information,\noften via a deceptive email."),("Phishing")),
    (("A wireless access point that provides an attacker with\nunauthorized access to the traffic going over the network."),("Rogue access point"))
]
