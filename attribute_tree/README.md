The [d3.tree](https://github.com/d3/d3-hierarchy/blob/master/README.md#tree) layout implements the Reingold-Tilford algorithm for efficient, tidy arrangement of layered nodes. The depth of nodes is computed by distance from the root, leading to a ragged appearance. Cartesian orientations are also supported. Implementation based on work by [Jeff Heer](http://jheer.org/) and [Jason Davies](http://www.jasondavies.com/) using [Buchheim et al.](http://www.springerlink.com/content/u73fyc4tlxp3uwt8/)’s linear-time variant of the Reingold-Tilford algorithm. Data shows the [Flare](http://flare.prefuse.org/) class hierarchy, also courtesy Jeff Heer.

Compare to this [Cartesian layout](/mbostock/4339184).

This [Gist fork](https://gist.github.com/swkasica/6c2b7784ec654b999397b8bc29b84c08) uses this visualization on a file systems' directory structure.