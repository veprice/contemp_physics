```<div id="glowscript" class="glowscript">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<link type="text/css" href="https://www.glowscript.org/css/redmond/2.1/jquery-ui.custom.css" rel="stylesheet" />
<link type="text/css" href="https://www.glowscript.org/css/ide.css" rel="stylesheet" />
<script type="text/javascript" src="https://www.glowscript.org/lib/jquery/2.1/jquery.min.js"></script>
<script type="text/javascript" src="https://www.glowscript.org/lib/jquery/2.1/jquery-ui.custom.min.js"></script>
<script type="text/javascript" src="https://www.glowscript.org/package/glow.3.2.min.js"></script>
<script type="text/javascript" src="https://www.glowscript.org/package/RSrun.3.2.min.js"></script>
<script type="text/javascript"><!--//--><![CDATA[//><!--

// START JAVASCRIPT
;(function() {;
var ρσ_modules = {};
ρσ_modules.pythonize = {};

(function(){
    function strings() {
        var string_funcs, exclude, name;
        string_funcs = set("capitalize strip lstrip rstrip islower isupper isspace lower upper swapcase center count endswith startswith find rfind index rindex format join ljust rjust partition rpartition replace split rsplit splitlines zfill".split(" "));
        if (!arguments.length) {
            exclude = (function(){
                var s = ρσ_set();
                s.jsset.add("split");
                s.jsset.add("replace");
                return s;
            })();
        } else if (arguments[0]) {
            exclude = Array.prototype.slice.call(arguments);
        } else {
            exclude = null;
        }
        if (exclude) {
            string_funcs = string_funcs.difference(set(exclude));
        }
        var ρσ_Iter0 = string_funcs;
        ρσ_Iter0 = ((typeof ρσ_Iter0[Symbol.iterator] === "function") ? (ρσ_Iter0 instanceof Map ? ρσ_Iter0.keys() : ρσ_Iter0) : Object.keys(ρσ_Iter0));
        for (var ρσ_Index0 of ρσ_Iter0) {
            name = ρσ_Index0;
            (ρσ_expr_temp = String.prototype)[(typeof name === "number" && name < 0) ? ρσ_expr_temp.length + name : name] = (ρσ_expr_temp = ρσ_str.prototype)[(typeof name === "number" && name < 0) ? ρσ_expr_temp.length + name : name];
        }
    };
    if (!strings.__module__) Object.defineProperties(strings, {
        __module__ : {value: "pythonize"}
    });

    ρσ_modules.pythonize.strings = strings;
})();
async function __main__() {
"use strict";
    var display = canvas;
    var scene = canvas();

    var version, print, arange, __name__, type, ρσ_ls, neutron, quarks, dt, tmax, t, vout, q;
    version = ρσ_list_decorate([ "3.2", "glowscript" ]);
    Array.prototype['+'] = function(r) {return this.concat(r)}
    Array.prototype['*'] = function(r) {return __array_times_number(this, r)}
    window.__GSlang = "vpython";
    print = GSprint;
    arange = range;
    __name__ = "__main__";
    type = pytype;
    var strings = ρσ_modules.pythonize.strings;

    strings();
    "6";
    neutron = ρσ_interpolate_kwargs.call(this, sphere, [ρσ_desugar_kwargs({opacity: .3})]);
    "9";
    async function q_init() {
        "10";
        return random()["-"](.5);
    };
    if (!q_init.__module__) Object.defineProperties(q_init, {
        __module__ : {value: null}
    });

    "13";
    quarks = ρσ_list_decorate([]);
    "15";
    quarks.append(ρσ_interpolate_kwargs.call(this, cone, [ρσ_desugar_kwargs({radius: .1, axis: vec(0, .2, 0), color: color.red, type: "up", pos: vec((await q_init()), (await q_init()), (await q_init())), v: vec((await q_init()), (await q_init()), (await q_init()))})]));
    "18";
    quarks.append(ρσ_interpolate_kwargs.call(this, cone, [ρσ_desugar_kwargs({radius: .1, axis: vec(0, .2["-u"](), 0), color: color.green, type: "down", pos: vec((await q_init()), (await q_init()), (await q_init())), v: vec((await q_init()), (await q_init()), (await q_init()))})]));
    "21";
    quarks.append(ρσ_interpolate_kwargs.call(this, cone, [ρσ_desugar_kwargs({radius: .1, axis: vec(0, .2["-u"](), 0), color: color.blue, type: "down", pos: vec((await q_init()), (await q_init()), (await q_init())), v: vec((await q_init()), (await q_init()), (await q_init()))})]));
    "26";
    dt = .05;
    "27";
    tmax = 10;
    "28";
    t = 0;
    "31";
    while (t["<"](tmax)) {
        "32";
        (await rate(40));
        "35";
        var ρσ_Iter1 = quarks;
        ρσ_Iter1 = ((typeof ρσ_Iter1[Symbol.iterator] === "function") ? (ρσ_Iter1 instanceof Map ? ρσ_Iter1.keys() : ρσ_Iter1) : Object.keys(ρσ_Iter1));
        for (var ρσ_Index1 of ρσ_Iter1) {
            q = ρσ_Index1;
            "36";
            q.pos=q.pos["+"](q.v["*"](dt));
            "37";
            vout = q.pos.dot(q.v)["/"](mag(q.pos));
            "40";
            if (mag(q.pos)[">"](1["-"](q.radius)) && vout[">"](0)) {
                "42";
                q.v = q.v["-"](2["*"](vout)["*"](q.pos)["/"](mag(q.pos)));
            }
        }
        "44";
        t=t["+"](dt);
    }
    "47";
    print("Done!");
};
if (!__main__.__module__) Object.defineProperties(__main__, {
    __module__ : {value: null}
});

;$(function(){ window.__context = { glowscript_container: $("#glowscript").removeAttr("id") }; __main__() })})()
// END JAVASCRIPT

//--><!]]></script>
</div>
```