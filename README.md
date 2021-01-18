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

We'll take some unrefactored code - the sample solution to [Codecademy's Games of Chance project](https://www.codecademy.com/practice/projects/games-of-chance) - and try to improve it through refactoring.

## Learning Outcomes

- Read and interpret somebody else's code
- Extract out reusable helper functions
- Articulate the DRY principle

## Exercise 1: Building the project yourself

**Success criterion:** you have built the Codecademy _Game of Chance_ project locally.

This is an optional exercise, but we think you will get more from subsequent exercises if you do this.

Firstly, you will need to create a new Codecademy account and sign up for a free 7-day Pro trial in order to access the [Codecademy Games of Chance Pro project](https://www.codecademy.com/practice/projects/games-of-chance). _Make sure you remember to cancel your trial before you are billed - you should be able to do this fairly immediately._

> N.B. If you have any barriers to starting a Codecademy Pro trial (e.g. an abundance of caution), please contact a member of Academy faculty.

Complete the project - but we encourage you to do it locally.

### Code smells

As you are building your project, try to be mindful of the following 'code smells' (i.e. symptoms of 'unclean' code):

- [Duplicate code](https://sourcemaking.com/refactoring/smells/duplicate-code)
- [Excessive comments](https://sourcemaking.com/refactoring/smells/comments)
- [Long functions](https://sourcemaking.com/refactoring/smells/long-method).

## Exercise 2: Reading a sample solution

**Success criterion:** a document which outlines your initial thoughts on the readability, strengths and weaknesses of a sample solution.

The file `original/main.py` has the official Codecademy sample solution for Games of Chance.

We'll be improving it through refactoring soon - but, for now, your task is only to _read_ it and collect some thoughts on the code.

Here are some prompts for you to consider:

1. **Quick big picture.** How skimmable is the code in the way that it is structured? (This is important because in a codebase you will want to have a big picture in mind, separate from the implementation details.)
2. **Clarity of intent.** How clear to you is the _intent_ of the code is? (This is important because code with clear intent makes it easier to fix e.g. a silly mistake, but it's very hard to fix or even spot bugs if you don't even know what the intended behaviour is.)
3. **Ease of navigation.** How easy is it for you to navigate around the code? (This is important because you can use your time more efficiently if you are working on a codebase that is easy to navigate.)

It will also help to consider the specific code smells listed above.

## Exercise 3: Writing your own Express route

> 🎯 **Success criterion:** you can visit `localhost:5050/hello-world`, `localhost:5050/ponies/random` and `localhost:5050/history` in the browser, with the expected behaviour (detailed below).

Now that you've been

### `/hello-world`

### `/ponies/random`

### `/history`

Can you populate it with some information about yourself (a short bio, maybe a CV-esque thing) and render the component through your React app?

(It's up to you as to whether you replace other bits of HTML or the other component, `MyFirstReactComponent`; all that's required is that you can see your component's rendered HTML. Don't forget that you'll need to refresh when you make changes!)

## Exercise 4: Check your understanding

> 🎯 **Success criterion:** a conversation with a Faculty member and amended comments.

Talk to a member of Faculty about your understanding of the game and of TypeScript.

Amend your notes for any important points that come out of the conversation.

## Exercise 5: Commentary and reflection

**Success criterion:** documented reflections.
