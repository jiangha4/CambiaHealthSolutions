## Testing Methodology

#### 1.
QAs role is to ensure the quality of the product that has been produced. QA should not be
nit picking the code, but should be more concerned with performace, usability, function,
and easy of use. QA's role is to find use case bugs that are hard to find through
automated function unit testing.

#### 2.
I would have the team create use cases and users for the product. Develop an idea for
who is using these products and what they might do with the product. From the use cases,
break the cases down into sub cases where a single test would be testing a single use case
or sub use case.

#### 3.
Automated testing is useful for test cases that use mutliple trials of the same action. It
is also useful for measuring performance and functionality of the product. However,
automated testing is painful if the infrastructure around the automated tests is not good.
Developers might spend more time debugging tests and figure out tests results rather than
actually getting good test feedback. Another feature of automated testing is the reduction
of costs. If things are being automated, you don't need to pay someone to do it.

But, automated testing cannot test the usability, easy of use, and the experience of using
the product. All this must be done with manual testing. The downside is, is that you have
to pay someone to do it.

#### 4.
For integration testing, I would first consider where my team added features and what parts
of the code base they touched. Then I would want to make a map of how these features interact
and create tests for these points of interaction. For components that do not interact, I
would skip those portions as the developer's unit tests should catch anything issues with
that feature.

