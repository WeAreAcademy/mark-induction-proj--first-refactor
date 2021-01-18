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

Firstly, you will need to create a new Codecademy account and sign up for a free 7-day trial in order to access the [Codecademy Games of Chance Pro project](https://www.codecademy.com/practice/projects/games-of-chance).

Complete the project - but we encourage you to do it locally.

## Exercise 2: Reading, understanding and documenting

**Success criterion:** a document which outlines how you think this Express server works. You don't have to achieve a theory which explains 100%, but you should strive to explain as much as possible.

(N.B.: The _correctness_ of your theory is **much less important** than the _process_ of forming this document. [Forming a prediction, and then discovering it was wrong, is an effective way to learn](https://www.sciencedirect.com/science/article/abs/pii/S0959475217303468)!)

1. Take some time to read and digest the code
2. Google things that you don't understand
3. Experiment with changing things
4. Produce a narrative document

A good narrative document for this game would explain what code gets executed when the server is started, and what code gets executed when different endpoints are hit - and how what you see in your browser (as the server response) either changes / does not change on subsequent requests depending on the route.

(Some routes will give you back the same response each time, and others won't. Why is that?)

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
