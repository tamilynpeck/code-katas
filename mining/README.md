# Problem:

A mining company wants to check to see if it has copper, silver, gold, or platinum in its mine. Given this Mine class:
`public class Mine
{
public static string COPPER = "copper";
public static string SILVER = "silver";
public static string GOLD = "gold";
public static string PLATINUM = "platinum";
public static string[] PRECIOUS = new[] { COPPER, SILVER, GOLD, PLATINUM };
public static string[] Ore = {
<item 1>,
<item 2>,
...,
<item N>
};
}`
Check each item in the Ore property to see if has randomly placed letters of a precious metal contained in it.

An Ore item may contain one or less precious metal. For example:

awopefijaOpwGeLgeegegD has the letters for gold. (The letters for gold where made uppercase for emphasis, but the actual data will all be lowercase.)

TODO:

- Find which items contain a precious metal.
- Print a report that show how many of each metal you've mined and how many of the ore items were empty.

Ore Item Count: 30
copper: 4
silver: 3
gold: 3
platinum: 5
empty: 15
