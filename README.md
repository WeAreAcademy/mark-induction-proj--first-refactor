---
module: mark-induction

level: 1

methods:
  - team
  - pair
  - solo

tags:
  - wip
---

# Game of Refactoring

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a>

> This is part of Academy's [technical curriculum for **The Mark**](https://github.com/WeAreAcademy/curriculum-mark). All parts of that curriculum, including this project, are licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.

We're going to look at how we might read, interpret and refactor somebody else's code.

We'll take some code and try to improve it through refactoring.

## Learning Outcomes

- Read and interpret somebody else's code
- Extract out reusable helper functions
- Articulate the DRY principle

## Exercise 1: Reading some sample code

> 🎯 **Success criterion:** a document which outlines your initial thoughts on the readability, strengths and weaknesses of a sample solution.

The file `original/main.py` has the some existing code.

We'll be improving it through refactoring soon - but, for now, your task is only to _read_ it and collect some thoughts on the code.

Here are some prompts for you to consider:

1. **Quick big picture.** How skimmable is the code in the way that it is structured? (This is important because in a codebase you will want to have a big picture in mind, separate from the implementation details.)
2. **Clarity of intent.** How clear to you is the _intent_ of the code is? (This is important because code with clear intent makes it easier to fix e.g. a silly mistake, but it's very hard to fix or even spot bugs if you don't even know what the intended behaviour is.)
3. **Ease of navigation.** How easy is it for you to navigate around the code? (This is important because you can use your time more efficiently if you are working on a codebase that is easy to navigate.)

**'Code smells'** to look out for:

- [Duplicate code](https://sourcemaking.com/refactoring/smells/duplicate-code)
- [Excessive comments](https://sourcemaking.com/refactoring/smells/comments)
- [Long functions](https://sourcemaking.com/refactoring/smells/long-method).

It might be helpful for you to note down where you see instances of this in the provided original code.

## Exercise 2: Refactoring an existing solution

> 🎯 **Success criterion:** a refactored version of the sample solution which removes identified code smells

Now you've been through the existing code, it's time to refactor it.

### Refactoring techniques

- [Consolidate Conditional Expression](https://sourcemaking.com/refactoring/consolidate-conditional-expression)
- [Decompose Conditional](https://sourcemaking.com/refactoring/decompose-conditional)
- [Extract Method](https://sourcemaking.com/refactoring/extract-method)
- [Extract Variable](https://sourcemaking.com/refactoring/extract-variable)

## Exercise 3: Sample refactoring investigation

The folder `refactored` has a sample refactoring of `original/main.py`.

Read through it with the same lens of above:

1. Quick big picture
2. Clarity of intent
3. Ease of navigation

What are the things which are better in this solution than the original one?

## Exercise 4: Check your understanding

> 🎯 **Success criterion:** a conversation with a Faculty member and amended comments.

Talk to a member of Faculty about your refactored solution and your understanding of code smells and refactoring techniques.

Amend your notes for any important points that come out of the conversation.

## Exercise 5: Commentary and reflection

**Success criterion:** documented reflections.
