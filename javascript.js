function search() {
    var needle = document.getElementById("searchForm").elements["searchItem"].value;
    needle = needle.toLowerCase();
    var source = document.getElementsByClassName("myTags");
    for (var s of source) if (s.textContent.toLowerCase().includes(needle))
        ancestors(s, 'details').forEach(e => e.open = true);
}

function ancestors(e, t) {
    var nodes = [];
    t = t.toUpperCase();
    while (e = e.parentNode) if (e.nodeName == t) nodes.push(e);
    return nodes;
}
